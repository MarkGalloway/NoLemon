import django_filters

from ..models import Advertisement


class AdvertisementFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')
    year = django_filters.NumberFilter(name="article__year", lookup_type='gte')
    mileage = django_filters.NumberFilter(name="article__mileage", lookup_type='lte')
    make = django_filters.CharFilter(name="article__car_model__make__make_type")
    model = django_filters.CharFilter(name="article__car_model__model_type")
    colour = django_filters.CharFilter(name="article__colour__basic_colour__colour_name")

    class Meta:
        model = Advertisement
        fields = ['make', 'model', 'min_price', 'max_price', 'year', 'mileage', 'colour']
