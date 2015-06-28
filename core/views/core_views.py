from django.views.generic import TemplateView


__all__ = ['HomePageView', 'SearchView', 'ProfileView', 'DetailView']

class HomePageView(TemplateView):
    template_name = 'landing.html'

class SearchView(TemplateView):
    template_name = 'search.html'

class DetailView(TemplateView):
    template_name = 'search-detail.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'