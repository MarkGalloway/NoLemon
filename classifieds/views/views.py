from rest_framework import viewsets, mixins, filters, renderers
from django.db.models import F

from ..models import Classified
from ..serializers import ClassifiedListSerializer
from .filters import ClassifiedFilter


class ClassifiedViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A ViewSet that for handling Classifieds

    Filtering:
        Custom filter (see ClassifiedFilter in filters.py)
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
    queryset = Classified.objects.all().select_related('vehicle', 'vehicle__car_model', 'vehicle__car_model__make',
                                                       'vehicle__colour', 'address', 'address__city', 'address__city__region',
                                                       'seller').prefetch_related('image').annotate(mileage=F('vehicle__mileage'))
    renderer_classes = (renderers.TemplateHTMLRenderer, renderers.JSONRenderer)
    template_name = 'ad_fragment.html'
    serializer_class = ClassifiedListSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    filter_class = ClassifiedFilter
    ordering_fields = ('date_posted', 'price', 'views', 'mileage')
    ordering = ('-date_posted', )
    search_fields = ('vehicle__description', 'vehicle__car_model__make__make_type', 'vehicle__car_model__model_type',
                     'vehicle__colour__basic_colour__colour_name')
