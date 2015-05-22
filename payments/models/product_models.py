from django.db import models

all = ['Product']


class Product(models.Model):
    """
    A model representing a Product
    """
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=256)
    price = models.IntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.name
