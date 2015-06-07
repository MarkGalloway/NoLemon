import datetime
from decimal import Decimal

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from model_mommy import mommy

from ..models import Advertisement
import vehicles.models as models
from ..serializers import AdvertisementListSerializer


class AdvertisementTestCase(APITestCase):
    """
    Superclass for testing the Advertisement behaviours
    """

    def setUp(self):
        """Initial testing data"""
        self.client = APIClient()

        # Basic Colour
        self.basic_blue = mommy.make(models.BasicColour, colour_name="Blue")
        self.basic_red = mommy.make(models.BasicColour, colour_name="Red")

        # Colour
        self.midnight_blue = mommy.make(models.Colour, colour_name="midnight blue", basic_colour=self.basic_blue)
        self.dark_blue = mommy.make(models.Colour, colour_name="dark blue", basic_colour=self.basic_blue)
        self.lipstick_red = mommy.make(models.Colour, colour_name="lipstick red", basic_colour=self.basic_red)

        # Makes
        self.make_toyota = mommy.make(models.Make, make_type="Toyota")
        self.make_honda = mommy.make(models.Make, make_type="Honda")

        # Models
        self.model_corolla = mommy.make(models.Model, model_type="Corolla", make=self.make_toyota)
        self.model_camry = mommy.make(models.Model, model_type="Camry", make=self.make_toyota)
        self.model_civic = mommy.make(models.Model, model_type="Civic", make=self.make_honda)

        # Vehicles
        self.vehicle_toyota_corolla = mommy.make(models.Vehicle, car_model=self.model_corolla,
                                                 year=2000, mileage=100000, colour=self.midnight_blue)
        self.vehicle_toyota_camry = mommy.make(models.Vehicle, car_model=self.model_camry,
                                               year=2010, mileage=10000, colour=self.dark_blue)
        self.vehicle_honda_civic = mommy.make(models.Vehicle, car_model=self.model_civic,
                                              year=1998, mileage=200000, colour=self.lipstick_red, description="A lemon")

        # Advertisements
        self.ad_corolla = mommy.make(Advertisement, price=5000, views=200, article=self.vehicle_toyota_corolla)
        self.ad_camry = mommy.make(Advertisement, price=9000, views=1, article=self.vehicle_toyota_camry)
        self.ad_civic = mommy.make(Advertisement, price=2000, views=5, article=self.vehicle_honda_civic)

        # override posted dates
        new_date = self.ad_civic.date_posted - datetime.timedelta(days=7)
        Advertisement.objects.filter(pk=self.ad_camry.id).update(date_posted=new_date)
        new_date = self.ad_civic.date_posted - datetime.timedelta(days=14)
        Advertisement.objects.filter(pk=self.ad_civic.id).update(date_posted=new_date)


class AdvertisementModelTests(AdvertisementTestCase):
    """
    Test Advertisement Model
    """
    def setUp(self):
        super(AdvertisementModelTests, self).setUp()


class AdvertisementManagerTests(AdvertisementTestCase):
    """
    Test Advertisement Manager
    """
    def setUp(self):
        super(AdvertisementManagerTests, self).setUp()


class AdvertisementSerializerTests(AdvertisementTestCase):
    """
    Test Advertisement Serializer
    """
    def setUp(self):
        super(AdvertisementSerializerTests, self).setUp()

    def test_serialization(self):
        ad = self.ad_corolla

        data = AdvertisementListSerializer(ad).data

        self.assertEquals(len(data), 7)
        self.assertEquals(Decimal(data.get('price', None)), ad.price)
        self.assertIsNotNone(data.get('date_posted', None))
        self.assertEquals(data.get('city', None), str(ad.address.city))
        self.assertEquals(data.get('seller_username', None), ad.seller.username)
        self.assertIsNotNone(data.get('article', None))
        self.assertIn('article', data)
        self.assertIn('image', data)


class AdvertisementViewTests(AdvertisementTestCase):
    """
    Test Advertisement Views
    """
    def setUp(self):
        super(AdvertisementViewTests, self).setUp()

    def test_list(self):
        ads = Advertisement.objects.all()
        response = self.client.get("/advertisements/")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

    def test_filter_min_price(self):
        # Assert ads >= $0
        ads = Advertisement.objects.all().filter(price__gte=0)
        response = self.client.get("/advertisements/?min_price=0")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

        # Assert ads >= $5000
        ads = Advertisement.objects.all().filter(price__gte=5000)
        response = self.client.get("/advertisements/?min_price=5000")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

        # Assert ads >= #9001
        ads = Advertisement.objects.all().filter(price__gte=9001)
        response = self.client.get("/advertisements/?min_price=9001")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

    def test_filter_max_price(self):
        # Assert ads <= $0
        ads = Advertisement.objects.all().filter(price__lte=0)
        response = self.client.get("/advertisements/?max_price=0")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

        # Assert ads <= $5000
        ads = Advertisement.objects.all().filter(price__lte=5000)
        response = self.client.get("/advertisements/?max_price=5000")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

        # Assert ads <= #9001
        ads = Advertisement.objects.all().filter(price__lte=9001)
        response = self.client.get("/advertisements/?max_price=9001")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

    def test_filter_year(self):
        ads = Advertisement.objects.all().filter(article__year__gte=2000)
        response = self.client.get("/advertisements/?year=2000")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_filter_mileage(self):
        ads = Advertisement.objects.all().filter(article__mileage__lte=100000)
        response = self.client.get("/advertisements/?mileage=100000")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_filter_car_model(self):
        ads = Advertisement.objects.all().filter(article__car_model__model_type="Corolla")
        response = self.client.get("/advertisements/?model=Corolla")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_filter_make(self):
        ads = Advertisement.objects.all().filter(article__car_model__make__make_type="Toyota")
        response = self.client.get("/advertisements/?make=Toyota")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_filter_colour(self):
        ads = Advertisement.objects.all().filter(article__colour__basic_colour__colour_name="Blue")
        response = self.client.get("/advertisements/?colour=Blue")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_filter_price_combination(self):
        # Assert ads == #5000
        ads = Advertisement.objects.all().filter(price__lte=5000).filter(price__gte=5000)
        response = self.client.get("/advertisements/?min_price=5000&max_price=5000")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_filter_combination(self):
        ads = Advertisement.objects.all()
        ads = ads.filter(price__lte=5000)
        ads = ads.filter(price__gte=5000)
        ads = ads.filter(article__colour__basic_colour__colour_name="Blue")
        ads = ads.filter(article__car_model__make__make_type="Toyota")
        ads = ads.filter(article__car_model__model_type="Corolla")
        ads = ads.filter(article__mileage__lte=100000)
        ads = ads.filter(article__year__gte=2000)
        query = "?min_price=5000&max_price=5000"
        query = query + "&colour=Blue"
        query = query + "&make=Toyota"
        query = query + "&model=Corolla"
        query = query + "&mileage=100000"
        query = query + "&year=2000"
        response = self.client.get("/advertisements/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_ordering_default(self):
        ads = Advertisement.objects.all().order_by('-date_posted')
        query = ""
        response = self.client.get("/advertisements/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        serializer = AdvertisementListSerializer(ads, many=True)
        self.assertEquals(data, serializer.data)

    def test_ordering_date_posted(self):
        ads = Advertisement.objects.all().order_by('date_posted')
        query = "?ordering=date_posted"
        response = self.client.get("/advertisements/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        serializer = AdvertisementListSerializer(ads, many=True)
        self.assertEquals(data, serializer.data)

    def test_ordering_price_decreasing(self):
        ads = Advertisement.objects.all().order_by('-price')
        query = "?ordering=-price"
        response = self.client.get("/advertisements/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        serializer = AdvertisementListSerializer(ads, many=True)
        self.assertEquals(data, serializer.data)

    def test_ordering_price_increasing(self):
        ads = Advertisement.objects.all().order_by('price')
        query = "?ordering=price"
        response = self.client.get("/advertisements/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        serializer = AdvertisementListSerializer(ads, many=True)
        self.assertEquals(data, serializer.data)

    def test_ordering_views_decreasing(self):
        ads = Advertisement.objects.all().order_by('-views')
        query = "?ordering=-views"
        response = self.client.get("/advertisements/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        serializer = AdvertisementListSerializer(ads, many=True)
        self.assertEquals(data, serializer.data)

    def test_ordering_views_increasing(self):
        ads = Advertisement.objects.all().order_by('views')
        query = "?ordering=views"
        response = self.client.get("/advertisements/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        serializer = AdvertisementListSerializer(ads, many=True)
        self.assertEquals(data, serializer.data)

    def test_search_make(self):
        ads = Advertisement.objects.all().filter(article__car_model__make__make_type="Toyota")
        query = "?search=toyota"
        response = self.client.get("/advertisements/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_search_model(self):
        ads = Advertisement.objects.all().filter(article__car_model__model_type="Civic")
        query = "?search=civic"
        response = self.client.get("/advertisements/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_search_make_and_model(self):
        ads = Advertisement.objects.all()
        ads = ads.filter(article__car_model__make__make_type="Toyota")
        ads = ads.filter(article__car_model__model_type="Corolla")
        query = "?search=toyota,corolla"
        response = self.client.get("/advertisements/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_search_partial_make_and_model(self):
        ads = Advertisement.objects.all()
        ads = ads.filter(article__car_model__make__make_type="Toyota")
        ads = ads.filter(article__car_model__model_type="Corolla")
        query = "?search=toy,cor"
        response = self.client.get("/advertisements/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_search_description(self):
        ads = Advertisement.objects.all()
        ads = ads.filter(article__car_model__make__make_type="Toyota")
        ads = ads.filter(article__car_model__model_type="Corolla")
        query = "?search=lemon"
        response = self.client.get("/advertisements/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_search_colour(self):
        ads = Advertisement.objects.all()
        ads = ads.filter(article__colour__basic_colour__colour_name="Blue")
        query = "?search=blue"
        response = self.client.get("/advertisements/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())
