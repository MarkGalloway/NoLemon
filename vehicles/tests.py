from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from model_mommy import mommy

import vehicles.models as models
from .serializers import VehicleSerializer


class VehicleTestCase(APITestCase):
    """
    Superclass for testing the Vehicle behaviours
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


class VehicleSerializerTests(VehicleTestCase):
    """
    Test Vehicle Serializer
    """
    def setUp(self):
        super(VehicleSerializerTests, self).setUp()

    def test_serialization(self):
        vehicle = self.vehicle_toyota_corolla

        data = VehicleSerializer(vehicle).data

        self.assertEquals(len(data), 10)
        self.assertEquals(data.get('description', None), vehicle.description)
        self.assertEquals(data.get('mileage', None), vehicle.mileage)
        self.assertEquals(data.get('year', None), vehicle.year)
        self.assertEquals(data.get('model', None), vehicle.car_model.model_type)
        self.assertEquals(data.get('make', None), vehicle.car_model.make.make_type)
        self.assertEquals(data.get('trim', None), vehicle.trim.trim_type)
        self.assertEquals(data.get('fuel_type', None), vehicle.fuel_type.fuel_type)
        self.assertEquals(data.get('transmission', None), vehicle.transmission.transmission_type)
        self.assertEquals(data.get('body', None), vehicle.body.body_type)
        self.assertIsNotNone(data.get('colour', None))
