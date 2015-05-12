from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

from audit_log.models.managers import AuditLog


class Model(models.Model):
    """
    Model representation for a `model` instance of a vehicle
    """
    model_type = models.CharField(max_length=30, null=False, blank=False, primary_key=True)

    audit_log = AuditLog()


class Make(models.Model):
    """
    Model representation for a `make` instance of a vehicle
    """
    make_type = models.CharField(max_length=30, null=False, blank=False, primary_key=True)

    audit_log = AuditLog()


class Trim(models.Model):
    """
    Model representation for a `trim` instance of a vehicle
    """
    trim_type = models.CharField(max_length=30, null=False, blank=False, primary_key=True)

    audit_log = AuditLog()


class Body(models.Model):
    """
    Model representation for a `body` instance of a vehicle
    """
    body_type = models.CharField(max_length=30, null=False, blank=False, primary_key=True)

    audit_log = AuditLog()


class Transmission(models.Model):
    """
    Model representation for a `transmission` instance of a vehicle
    """
    transmission_type = models.CharField(max_length=30, null=False, blank=False, primary_key=True)

    audit_log = AuditLog()


class Fuel(models.Model):
    """
    Model representation for a `fuel` instance of a vehicle
    """
    fuel_type = models.CharField(max_length=30, null=False, blank=False, primary_key=True)

    audit_log = AuditLog()


class BasicColour(models.Model):
    """
    Model representation for a `basic_colour` instance of a vehicle
    """
    colour_name = models.CharField(max_length=30, null=False, blank=False, primary_key=True)

    audit_log = AuditLog()


class Colour(models.Model):
    """
    Model representation for a `colour` instance of a vehicle
    """
    colour_name = models.CharField(max_length=30, null=False, blank=False, primary_key=True)
    basic_colour = models.ForeignKey(BasicColour, related_name="basic_colour")

    audit_log = AuditLog()


class Vehicle(models.Model):
    """
    Model representation for a `vehicle` instance
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="owner")
    description = models.CharField(max_length=250, null=False, blank=True)
    model = models.ForeignKey(Model)
    make = models.ForeignKey(Make)
    trim = models.ForeignKey(Trim)
    body = models.ForeignKey(Body)
    transmission = models.ForeignKey(Transmission)
    fuel_type = models.ForeignKey(Fuel)
    colour = models.ForeignKey(Colour)
    mileage = models.IntegerField(null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
