import django_filters

from ..models import Classified


class ClassifiedFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')
    year = django_filters.NumberFilter(name="vehicle__year", lookup_type='gte')
    mileage = django_filters.NumberFilter(name="vehicle__mileage", lookup_type='lte')
    make = django_filters.CharFilter(name="vehicle__car_model__make__make_type")
    model = django_filters.CharFilter(name="vehicle__car_model__model_type")
    colour = django_filters.CharFilter(name="vehicle__colour__basic_colour__colour_name")

    class Meta:
        model = Classified
        fields = ['make', 'model', 'min_price', 'max_price', 'year', 'mileage', 'colour']
