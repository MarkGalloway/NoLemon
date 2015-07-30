import django_filters

from ..models import Classified


class ClassifiedFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')
    min_year = django_filters.NumberFilter(name="vehicle__year", lookup_type='gte')
    max_year = django_filters.NumberFilter(name="vehicle__year", lookup_type='lte')
    min_mileage = django_filters.NumberFilter(name="vehicle__mileage", lookup_type='gte')
    max_mileage = django_filters.NumberFilter(name="vehicle__mileage", lookup_type='lte')
    make = django_filters.CharFilter(name="vehicle__car_model__make__make_type")
    model = django_filters.CharFilter(name="vehicle__car_model__model_type")
    colour = django_filters.CharFilter(name="vehicle__colour__basic_colour__colour_name")

    class Meta:
        model = Classified
        fields = ['make', 'model', 'min_price', 'max_price', 'min_year', 'max_year', 'min_mileage', 'max_mileage', 'colour']
