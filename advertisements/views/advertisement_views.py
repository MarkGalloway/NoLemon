from rest_framework import viewsets, mixins, filters

from ..models import Advertisement
from ..serializers import AdvertisementListSerializer
from .filters import AdvertisementFilter


class AdvertisementViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A ViewSet that for handling Advertisements

    Filtering:
        Custom filter (see AdvertisementFilter in filters.py)
            http://example.com/api/ads?max_price=30&min_price=10&

    Ordering:
        default ordering specified by `ordering` attribute
        specify ordering by allowed fields `ordering_fields` in the url as such:
            http://example.com/api/users?ordering=-price
        Multiple orderings can be used by comma separation:
            http://example.com/api/users?ordering=-price,date_posted,views

    Searching:
        By default, searches will use case-insensitive partial matches.
        The search parameter may contain multiple search terms, which should be whitespace
        and/or comma separated. If multiple search terms are used then objects will be
        returned in the list only if all the provided terms are matched.
            ?search=toyota
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementListSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    filter_class = AdvertisementFilter
    ordering_fields = ('date_posted', 'price', 'views')
    ordering = ('-date_posted', )
    search_fields = ('article__description', 'article__car_model__make__make_type', 'article__car_model__model_type',
                     'article__colour__basic_colour__colour_name')
