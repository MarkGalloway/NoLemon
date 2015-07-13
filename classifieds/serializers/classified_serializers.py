from django.utils.timesince import timesince
from rest_framework import serializers

from ..models import Classified
from vehicles.serializers import VehicleSerializer

__all__ = ['ClassifiedListSerializer']


class ClassifiedListSerializer(serializers.ModelSerializer):
    """
    Serializer for an instance of the Classified model
    """
    city = serializers.CharField(max_length=30, source='address.city')
    region = serializers.CharField(max_length=30, source='address.city.region')
    date_posted = serializers.SerializerMethodField()
    vehicle = VehicleSerializer()

    def get_date_posted(self, obj):
       return timesince(obj.date_posted)

    class Meta:
        model = Classified
        fields = ('id', 'price', 'city', 'region', 'vehicle', 'image', 'date_posted')
        depth = 2
