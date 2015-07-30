from django.views.generic import TemplateView
from django.views.decorators.vary import vary_on_headers

from classifieds.views import ClassifiedViewSet

__all__ = ['HomePageView', 'SearchView', 'ProfileView', 'DetailView']


class HomePageView(TemplateView):
    template_name = 'landing.html'


class SearchView(TemplateView):
    template_name = 'search.html'

    @vary_on_headers('X-Requested-With')
    def dispatch(self, *args, **kwargs):
        return super(SearchView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        super(TemplateView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        # Delegate ajax request to DRF view
        if request.is_ajax():
            return ClassifiedViewSet.as_view({'get': 'list'})(request)
        return super(SearchView, self).get(request, *args, **kwargs)


class DetailView(TemplateView):
    template_name = 'search-detail.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'
