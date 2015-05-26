from django.db import models

from .product_models import Product
from core.models import User, Address

__all__ = ['PaymentProfile', 'Receipt']


class PaymentProfile(models.Model):
    """
    A model representing the payment information of a user
    """
    user = models.ForeignKey(User, related_name="payment_profiles")
    address = models.ForeignKey(Address, related_name="payment_profiles")
    phone = models.CharField(max_length=10)


class Receipt(models.Model):
    """
    A model representing the Receipt of a payment
    """
    user = models.ForeignKey(User, related_name="receipts")
    products = models.ManyToManyField(Product, related_name="receipts")
    payment_profile = models.ForeignKey(PaymentProfile, related_name="receipts")
    total = models.DecimalField(max_digits=6, decimal_places=2)
    payment_complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
