from rest_framework import serializers

from ..models import Vehicle

__all__ = ['VehicleSerializer']


class VehicleSerializer(serializers.ModelSerializer):
    """
    Serializer for an instance of the Vehicle model
    """
    model = serializers.CharField(max_length=30, source='car_model.model_type')
    make = serializers.CharField(max_length=30, source='car_model.make.make_type')
    colour = serializers.CharField(max_length=30, source='colour.colour_name')

    class Meta:
        model = Vehicle
        fields = ('model', 'make', 'colour', 'mileage', 'year')
        depth = 1
