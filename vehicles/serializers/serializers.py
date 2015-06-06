from rest_framework import serializers

from ..models import Vehicle

__all__ = ['VehicleSerializer']


class VehicleSerializer(serializers.ModelSerializer):
    """
    Serializer for an instance of the Vehicle model
    """
    model = serializers.CharField(max_length=30, source='car_model.model_type')
    make = serializers.CharField(max_length=30, source='car_model.make.make_type')
    trim = serializers.CharField(max_length=30, source='trim.trim_type')
    transmission = serializers.CharField(max_length=30, source='transmission.transmission_type')
    body = serializers.CharField(max_length=30, source='body.body_type')
    fuel_type = serializers.CharField(max_length=30, source='fuel_type.fuel_type')

    class Meta:
        model = Vehicle
        fields = ('description', 'model', 'make', 'trim', 'body', 'transmission',
                  'fuel_type', 'colour', 'mileage', 'year')
        depth = 1
