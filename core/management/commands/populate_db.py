import datetime
from model_mommy import mommy

from django.core.management.base import BaseCommand

from classifieds import models as ad_models
from vehicles import models as car_models
from core import models as core_models


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_bulk_data(self):
        pass

    def _test_dataset_one(self):
        """ Test Data Set One
        Populates 3 advertisements with 3 unique vehicles
        """

        # Region
        self.alberta = mommy.make(core_models.Region, name="Alberta")

        # City
        self.sherwood_park = mommy.make(core_models.City, name="Sherwood Park", region=self.alberta)
        self.edmonton = mommy.make(core_models.City, name="Edmonton", region=self.alberta)
        self.st_albert = mommy.make(core_models.City, name="St. Albert", region=self.alberta)

        # Address
        self.address1 = mommy.make(core_models.Address, city=self.sherwood_park)
        self.address2 = mommy.make(core_models.Address, city=self.st_albert)
        self.address3 = mommy.make(core_models.Address, city=self.edmonton)

        # Basic Colours
        self.basic_blue = mommy.make(car_models.BasicColour, colour_name="Blue")
        self.basic_red = mommy.make(car_models.BasicColour, colour_name="Red")

        # Colours
        self.midnight_blue = mommy.make(car_models.Colour, colour_name="Midnight Blue", basic_colour=self.basic_blue)
        self.dark_blue = mommy.make(car_models.Colour, colour_name="Dark Blue", basic_colour=self.basic_blue)
        self.lipstick_red = mommy.make(car_models.Colour, colour_name="Lipstick Red", basic_colour=self.basic_red)

        # Makes
        self.make_toyota = mommy.make(car_models.Make, make_type="Toyota")
        self.make_honda = mommy.make(car_models.Make, make_type="Honda")

        # Models
        self.model_corolla = mommy.make(car_models.Model, model_type="Corolla", make=self.make_toyota)
        self.model_camry = mommy.make(car_models.Model, model_type="Camry", make=self.make_toyota)
        self.model_civic = mommy.make(car_models.Model, model_type="Civic", make=self.make_honda)

        # Vehicles
        self.vehicle_toyota_corolla = mommy.make(car_models.Vehicle, car_model=self.model_corolla,
                                                 year=2000, mileage=100000, colour=self.midnight_blue)
        self.vehicle_toyota_camry = mommy.make(car_models.Vehicle, car_model=self.model_camry,
                                               year=2010, mileage=10000, colour=self.dark_blue)
        self.vehicle_honda_civic = mommy.make(car_models.Vehicle, car_model=self.model_civic,
                                              year=1998, mileage=200000, colour=self.lipstick_red, description="A lemon")

        # Advertisements
        self.ad_corolla = mommy.make(ad_models.Classified, price=5000, views=200, vehicle=self.vehicle_toyota_corolla,
                                     address=self.address1)
        self.ad_camry = mommy.make(ad_models.Classified, price=9000, views=1, vehicle=self.vehicle_toyota_camry,
                                     address=self.address2)
        self.ad_civic = mommy.make(ad_models.Classified, price=2000, views=5, vehicle=self.vehicle_honda_civic,
                                     address=self.address3)

        # override posted dates
        new_date = self.ad_civic.date_posted - datetime.timedelta(days=7)
        ad_models.Classified.objects.filter(pk=self.ad_camry.id).update(date_posted=new_date)
        new_date = self.ad_civic.date_posted - datetime.timedelta(days=14)
        ad_models.Classified.objects.filter(pk=self.ad_civic.id).update(date_posted=new_date)

    def handle(self, *args, **options):

        # Specific test data
        self._test_dataset_one()

        # Create Bulk Data for DB load
        # self._create_bulk_data()
