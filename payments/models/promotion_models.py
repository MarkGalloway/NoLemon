from django.db import models

from . import Product

__all__ = ['Promotion']


class Promotion(models.Model):
    """
    A model representing the promotion of a Product
    """
    name = models.CharField(max_length=30)
    product = models.ForeignKey(Product, related_name="promotions")
    description = models.CharField(max_length=256)
    promo_code = models.IntegerField(null=True)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField()
    start_date = models.DateTimeField()
    expiration_date = models.DateTimeField()

    def __str__(self):
        return self.name
