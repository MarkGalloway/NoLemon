import time
from hashids import Hashids

from django.db import models
from django.db import IntegrityError
from django import forms
from django.contrib.auth.models import Group
from core.models import phone_validator


__all__ = ['Inspection', 'Shop']

hashids = Hashids('23456789ABCDEFGHIJKLMNPQRSTUVQXYZabdefghijpqrtqy')


def generate_referral_code():
    # encode the timestamp in nano seconds
    hashids.encode(int(time.time() * 1000))

class Shop(models.Model):
    """
    A model representing a mechanic shop
    """

    name = models.CharField(max_length=70)
    group = models.OneToOneField(Group, null=True, blank=True)
    phone = models.CharField(max_length=15, default="", blank=True, validators=[phone_validator])
    address = models.ForeignKey('core.Address')

    def __str__(self):
        return self.name


class Inspection(models.Model):
    """
    A model representing a No Lemon inspection
    """
    id = models.CharField(max_length=10, primary_key=True, default=generate_referral_code)
    user = models.ForeignKey('core.User', related_name="inspections")
    shop = models.ForeignKey('Shop', verbose_name='Technician Shop', related_name="inspections")
    vehicle = models.ForeignKey('vehicles.Vehicle', related_name="inspections")
    date_completed = models.DateTimeField(blank=True, null=True)

    CHOICES = [(1,'Good'), (2,'Fair'), (3, 'Poor')]
    CHOICES_OPTIONAL = [(0,'N/A')] + CHOICES

    # Exterior
    windshield = models.PositiveSmallIntegerField(choices=CHOICES, default=3)
    wipers = models.PositiveSmallIntegerField(choices=CHOICES, default=3)
    windows = models.PositiveSmallIntegerField(choices=CHOICES, default=3)
    mirrors = models.PositiveSmallIntegerField(choices=CHOICES, default=3)
    exterior_condition = models.PositiveSmallIntegerField(choices=CHOICES, default=3)

    # Lights
    headlights = models.PositiveSmallIntegerField(choices=CHOICES, default=3)
    fog_lights = models.PositiveSmallIntegerField(choices=CHOICES, default=3)
    signal_lights = models.PositiveSmallIntegerField(choices=CHOICES, default=3)
    hazard_lights = models.PositiveSmallIntegerField(choices=CHOICES, default=3)
    backup_lights = models.PositiveSmallIntegerField(choices=CHOICES, default=3)
    dome_lights = models.PositiveSmallIntegerField(choices=CHOICES, default=3)

    trunk_light = models.PositiveSmallIntegerField(choices=CHOICES_OPTIONAL, default=3)
    license_light = models.PositiveSmallIntegerField(choices=CHOICES_OPTIONAL, default=3)

    exterior_notes = models.TextField('Notes', blank=True, default="")
    technician = models.CharField(max_length=70, blank=False, null=False)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        unique = False
        while not unique:
            try:
                super(Inspection, self).save(*args, **kwargs)
            except IntegrityError:
                self.code = generate_referral_code()
            else:
                unique = True