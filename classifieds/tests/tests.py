import datetime
from decimal import Decimal

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from model_mommy import mommy

from ..models import Classified
import vehicles.models as models
from ..serializers import ClassifiedListSerializer


class ClassifiedTestCase(APITestCase):
    """
    Superclass for testing the Classified behaviours
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

        # Classifieds
        self.ad_corolla = mommy.make(Classified, price=5000, views=200, vehicle=self.vehicle_toyota_corolla)
        self.ad_camry = mommy.make(Classified, price=9000, views=1, vehicle=self.vehicle_toyota_camry)
        self.ad_civic = mommy.make(Classified, price=2000, views=5, vehicle=self.vehicle_honda_civic)

        # override posted dates
        new_date = self.ad_civic.date_posted - datetime.timedelta(days=7)
        Classified.objects.filter(pk=self.ad_camry.id).update(date_posted=new_date)
        new_date = self.ad_civic.date_posted - datetime.timedelta(days=14)
        Classified.objects.filter(pk=self.ad_civic.id).update(date_posted=new_date)


class ClassifiedModelTests(ClassifiedTestCase):
    """
    Test Classified Model
    """
    def setUp(self):
        super(ClassifiedModelTests, self).setUp()


class ClassifiedManagerTests(ClassifiedTestCase):
    """
    Test Classified Manager
    """
    def setUp(self):
        super(ClassifiedManagerTests, self).setUp()


class ClassifiedSerializerTests(ClassifiedTestCase):
    """
    Test Classified Serializer
    """
    def setUp(self):
        super(ClassifiedSerializerTests, self).setUp()

    def test_serialization(self):
        ad = self.ad_corolla

        data = ClassifiedListSerializer(ad).data

        self.assertEquals(Decimal(data.get('price', None)), ad.price)
        self.assertIsNotNone(data.get('date_posted', None))
        self.assertEquals(data.get('city', None), str(ad.address.city))
        self.assertIn('vehicle', data)
        self.assertIn('image', data)


class ClassifiedViewTests(ClassifiedTestCase):
    """
    Test Classified Views
    """
    def setUp(self):
        super(ClassifiedViewTests, self).setUp()

    def test_list(self):
        ads = Classified.objects.all()
        response = self.client.get("/classifieds/")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

    def test_filter_min_price(self):
        # Assert ads >= $0
        ads = Classified.objects.all().filter(price__gte=0)
        response = self.client.get("/classifieds/?min_price=0")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

        # Assert ads >= $5000
        ads = Classified.objects.all().filter(price__gte=5000)
        response = self.client.get("/classifieds/?min_price=5000")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

        # Assert ads >= #9001
        ads = Classified.objects.all().filter(price__gte=9001)
        response = self.client.get("/classifieds/?min_price=9001")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

    def test_filter_max_price(self):
        # Assert ads <= $0
        ads = Classified.objects.all().filter(price__lte=0)
        response = self.client.get("/classifieds/?max_price=0")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

        # Assert ads <= $5000
        ads = Classified.objects.all().filter(price__lte=5000)
        response = self.client.get("/classifieds/?max_price=5000")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

        # Assert ads <= #9001
        ads = Classified.objects.all().filter(price__lte=9001)
        response = self.client.get("/classifieds/?max_price=9001")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())

    def test_filter_year(self):
        ads = Classified.objects.all().filter(vehicle__year__gte=2000)
        response = self.client.get("/classifieds/?year=2000")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_filter_mileage(self):
        ads = Classified.objects.all().filter(vehicle__mileage__lte=100000)
        response = self.client.get("/classifieds/?mileage=100000")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_filter_car_model(self):
        ads = Classified.objects.all().filter(vehicle__car_model__model_type="Corolla")
        response = self.client.get("/classifieds/?model=Corolla")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_filter_make(self):
        ads = Classified.objects.all().filter(vehicle__car_model__make__make_type="Toyota")
        response = self.client.get("/classifieds/?make=Toyota")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_filter_colour(self):
        ads = Classified.objects.all().filter(vehicle__colour__basic_colour__colour_name="Blue")
        response = self.client.get("/classifieds/?colour=Blue")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_filter_price_combination(self):
        # Assert ads == #5000
        ads = Classified.objects.all().filter(price__lte=5000).filter(price__gte=5000)
        response = self.client.get("/classifieds/?min_price=5000&max_price=5000")

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_filter_combination(self):
        ads = Classified.objects.all()
        ads = ads.filter(price__lte=5000)
        ads = ads.filter(price__gte=5000)
        ads = ads.filter(vehicle__colour__basic_colour__colour_name="Blue")
        ads = ads.filter(vehicle__car_model__make__make_type="Toyota")
        ads = ads.filter(vehicle__car_model__model_type="Corolla")
        ads = ads.filter(vehicle__mileage__lte=100000)
        ads = ads.filter(vehicle__year__gte=2000)
        query = "?min_price=5000&max_price=5000"
        query = query + "&colour=Blue"
        query = query + "&make=Toyota"
        query = query + "&model=Corolla"
        query = query + "&mileage=100000"
        query = query + "&year=2000"
        response = self.client.get("/classifieds/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_ordering_default(self):
        ads = Classified.objects.all().order_by('-date_posted')
        query = ""
        response = self.client.get("/classifieds/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        serializer = ClassifiedListSerializer(ads, many=True)
        self.assertEquals(data, serializer.data)

    def test_ordering_date_posted(self):
        ads = Classified.objects.all().order_by('date_posted')
        query = "?ordering=date_posted"
        response = self.client.get("/classifieds/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        serializer = ClassifiedListSerializer(ads, many=True)
        self.assertEquals(data, serializer.data)

    def test_ordering_price_decreasing(self):
        ads = Classified.objects.all().order_by('-price')
        query = "?ordering=-price"
        response = self.client.get("/classifieds/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        serializer = ClassifiedListSerializer(ads, many=True)
        self.assertEquals(data, serializer.data)

    def test_ordering_price_increasing(self):
        ads = Classified.objects.all().order_by('price')
        query = "?ordering=price"
        response = self.client.get("/classifieds/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        serializer = ClassifiedListSerializer(ads, many=True)
        self.assertEquals(data, serializer.data)

    def test_ordering_views_decreasing(self):
        ads = Classified.objects.all().order_by('-views')
        query = "?ordering=-views"
        response = self.client.get("/classifieds/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        serializer = ClassifiedListSerializer(ads, many=True)
        self.assertEquals(data, serializer.data)

    def test_ordering_views_increasing(self):
        ads = Classified.objects.all().order_by('views')
        query = "?ordering=views"
        response = self.client.get("/classifieds/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        serializer = ClassifiedListSerializer(ads, many=True)
        self.assertEquals(data, serializer.data)

    def test_search_make(self):
        ads = Classified.objects.all().filter(vehicle__car_model__make__make_type="Toyota")
        query = "?search=toyota"
        response = self.client.get("/classifieds/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_search_model(self):
        ads = Classified.objects.all().filter(vehicle__car_model__model_type="Civic")
        query = "?search=civic"
        response = self.client.get("/classifieds/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_search_make_and_model(self):
        ads = Classified.objects.all()
        ads = ads.filter(vehicle__car_model__make__make_type="Toyota")
        ads = ads.filter(vehicle__car_model__model_type="Corolla")
        query = "?search=toyota,corolla"
        response = self.client.get("/classifieds/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_search_partial_make_and_model(self):
        ads = Classified.objects.all()
        ads = ads.filter(vehicle__car_model__make__make_type="Toyota")
        ads = ads.filter(vehicle__car_model__model_type="Corolla")
        query = "?search=toy,cor"
        response = self.client.get("/classifieds/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_search_description(self):
        ads = Classified.objects.all()
        ads = ads.filter(vehicle__car_model__make__make_type="Toyota")
        ads = ads.filter(vehicle__car_model__model_type="Corolla")
        query = "?search=lemon"
        response = self.client.get("/classifieds/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())

    def test_search_colour(self):
        ads = Classified.objects.all()
        ads = ads.filter(vehicle__colour__basic_colour__colour_name="Blue")
        query = "?search=blue"
        response = self.client.get("/classifieds/" + query)

        # Assert response
        self.assertTrue(status.is_success(response.status_code))

        # Assert content
        data = response.data['results']
        self.assertEquals(len(data), ads.count())
        self.assertNotEquals(0, ads.count())
