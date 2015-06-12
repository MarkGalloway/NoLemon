from django.views.generic import TemplateView


__all__ = ['HomePageView', 'SearchView']

class HomePageView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        super(TemplateView, self).get_context_data(**kwargs)

class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        super(TemplateView, self).get_context_data(**kwargs)