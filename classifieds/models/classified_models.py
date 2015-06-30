from datetime import datetime

from django.db import models

from core.models import User, Address
from vehicles.models import Vehicle
from .media_models import Image

__all__ = ['Classified']


class ClassifiedQuerySet(models.QuerySet):
    """
    Custom QuerySet for the ClassifiedManager
    """
    def active(self):
        """Query to return only active Ad instances"""
        return self.filter(is_active=True)


class ClassifiedManager(models.Manager):
    """
    A custom manager for the Classified model
    """
    use_for_related_fields = True

    def get_queryset(self):
        return ClassifiedQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()


class Classified(models.Model):
    """
    A models representing an `Advertistement` instance
    """
    vehicle = models.ForeignKey(Vehicle, related_name="classifieds")
    seller = models.ForeignKey(User, related_name="classifieds")
    # inspection_report = models.ForeignKey(InspectionReport, related_name="ads")
    # history_report = models.ForeignKey(HistoryReport, related_name="ads")
    price = models.PositiveIntegerField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField(null=True)
    address = models.ForeignKey(Address, related_name="classifieds")
    image = models.ManyToManyField(Image, related_name="classifieds", through="ClassifiedImage")
    views = models.PositiveIntegerField(default=0)

    # Managers
    objects = ClassifiedManager()

    def delete(self, *args, **kwargs):
        """
        Custom delete to mark Ads as inactive (soft delete)
        """
        is_active = False
        date_closed = datetime.now()


class ClassifiedImage(models.Model):
    """
    Model for representing the Many to Many relationship
    between Classifieds and Images
    """
    image = models.ForeignKey(Image)
    classified = models.ForeignKey(Classified)
    order = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
