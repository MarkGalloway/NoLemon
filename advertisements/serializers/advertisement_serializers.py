from rest_framework import serializers

from ..models import Advertisement
from vehicles.serializers import VehicleSerializer

__all__ = ['AdvertisementListSerializer']


class AdvertisementListSerializer(serializers.ModelSerializer):
    """
    Serializer for an instance of the Advertisement model
    """
    city = serializers.CharField(max_length=30, source='address.city')
    seller_username = serializers.CharField(max_length=30, source='seller.username')
    article = VehicleSerializer()

    class Meta:
        model = Advertisement
        fields = ('id', 'price', 'date_posted', 'city', 'article', 'seller_username', 'image')
        depth = 2
