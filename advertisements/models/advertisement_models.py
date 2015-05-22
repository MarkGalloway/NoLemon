from datetime import datetime

from django.db import models

from core.models import User, Address
# from vehicles.models import Vehicle as Article
from .media_models import Image

__all__ = ['Advertisement']


class AdvertisementQuerySet(models.QuerySet):
    """
    Custom QuerySet for the AdvertisementManager
    """
    def active(self):
        """Query to return only active Ad instances"""
        return self.filter(is_active=True)


class AdvertisementManager(models.Manager):
    """
    A custom manager for the Advertisement model
    """
    use_for_related_fields = True

    def get_queryset(self):
        return AdvertisementQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()


class Advertisement(models.Model):
    """
    A models representing an `Advertistement` instance
    """
    # article = models.ForeignKey(Article, related_name="advertisements")
    seller = models.ForeignKey(User, related_name="advertisements")
    # inspection_report = models.ForeignKey(InspectionReport, related_name="ads")
    # history_report = models.ForeignKey(HistoryReport, related_name="ads")
    price = models.DecimalField(max_digits=11, decimal_places=2)
    is_active = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField(null=True)
    address = models.ForeignKey(Address, related_name="advertisements")
    image = models.ManyToManyField(Image, related_name="advertisements", through="AdvertisementImage")

    # Managers
    objects = AdvertisementManager()

    def delete(self, *args, **kwargs):
        """
        Custom delete to mark Ads as inactive (soft delete)
        """
        is_active = False
        date_closed = datetime.now()


class AdvertisementImage(models.Model):
    """
    Model for representing the Many to Many relationship
    between Advertisements and Images
    """
    image = models.ForeignKey(Image)
    advertisement = models.ForeignKey(Advertisement)
    order = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
