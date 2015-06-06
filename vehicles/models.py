from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

from simple_history.models import HistoricalRecords


class Make(models.Model):
    """
    Model representation for a `make` instance of a vehicle
    """
    make_type = models.CharField(max_length=30, null=False, blank=False, primary_key=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.make_type


class Model(models.Model):
    """
    Model representation for a `model` instance of a vehicle
    """
    make = models.ForeignKey(Make, related_name="models")
    model_type = models.CharField(max_length=30, null=False, blank=False, primary_key=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.model_type


class Trim(models.Model):
    """
    Model representation for a `trim` instance of a vehicle
    """
    trim_type = models.CharField(max_length=30, null=False, blank=False, primary_key=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.trim_type


class Body(models.Model):
    """
    Model representation for a `body` instance of a vehicle
    """
    body_type = models.CharField(max_length=30, null=False, blank=False, primary_key=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.body_type


class Transmission(models.Model):
    """
    Model representation for a `transmission` instance of a vehicle
    """
    transmission_type = models.CharField(max_length=30, null=False, blank=False, primary_key=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.transmission_type


class Fuel(models.Model):
    """
    Model representation for a `fuel` instance of a vehicle
    """
    fuel_type = models.CharField(max_length=30, null=False, blank=False, primary_key=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.fuel_type


class BasicColour(models.Model):
    """
    Model representation for a `basic_colour` instance of a vehicle
    """
    colour_name = models.CharField(max_length=30, null=False, blank=False, primary_key=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.colour_name


class Colour(models.Model):
    """
    Model representation for a `colour` instance of a vehicle
    """
    colour_name = models.CharField(max_length=30, null=False, blank=False, primary_key=True)
    basic_colour = models.ForeignKey(BasicColour, related_name="colours")
    history = HistoricalRecords()

    def __str__(self):
        return self.colour_name


class Vehicle(models.Model):
    """
    Model representation for a `vehicle` instance
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="owner")
    description = models.CharField(max_length=250, null=False, blank=True)
    car_model = models.ForeignKey(Model)
    trim = models.ForeignKey(Trim)
    body = models.ForeignKey(Body)
    transmission = models.ForeignKey(Transmission)
    fuel_type = models.ForeignKey(Fuel)
    colour = models.ForeignKey(Colour)
    mileage = models.PositiveIntegerField(null=False, blank=False)
    year = models.PositiveIntegerField(null=False, blank=False)
    history = HistoricalRecords()
