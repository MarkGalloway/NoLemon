from django.db import models

__all__ = ['Address', 'City', 'Region', 'Country']


class Country(models.Model):
    """Model representing a country"""
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Region(models.Model):
    """Model representing a Province/State"""
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country, related_name='regions')

    def __str__(self):
        return self.name


class City(models.Model):
    """Model representing a City"""
    name = models.CharField(max_length=128)
    region = models.ForeignKey(Region, related_name='cities')

    def __str__(self):
        return self.name


class Address(models.Model):
    """Model representing an Address"""
    city = models.ForeignKey(City, related_name='addresses')
    street_address = models.CharField(max_length=256)
    street_address2 = models.CharField(max_length=256)
    postal_code = models.CharField(max_length=9)

    def __str__(self):
        output = self.street_address

        if self.street_address2:
            output += ", " + self.street_address2

        output += ", " + self.city
        output += ", " + self.city.region
        output += ", " + self.city.region.country
        output += ", " + self.postal_code

        return output
