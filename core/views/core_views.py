from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from classifieds.views import ClassifiedViewSet


__all__ = ['AjaxFormMixin', 'AjaxValidateView', 'AjaxFormView', 'HomePageView', 'SearchView', 'ProfileView', 'DetailView']


class AjaxFormMixin(object):
    """
    form-template: Used to specify the template that will be returned by ajax.
    See inspection/ajax_1 for an example
    form_class: the form class used by the template
    """
    ajax_template = None
    form_class = None

    def get_form_kwargs(self, request):
        """
        Hook for passing arguments to the form class.
        """
        return {}


class AjaxValidateView(AjaxFormMixin, View):
    """
    View for handling ajax form submission.
    """

    def post(self, request, *args, **kwargs):
        form_kwargs = self.get_form_kwargs(request)
        form = self.form_class(request.POST, request.FILES, **form_kwargs)

        if not form.is_valid():
            response_data = {'form-content': render_to_string(self.ajax_template, {"form" : form})}
            return JsonResponse(response_data, status=400)

        obj = form.save(commit=True)
        return JsonResponse({}, status=200)


class AjaxFormView(AjaxFormMixin, TemplateView):
    """
    View for initially rendering a page with an ajax form.
    """

    template_name = None
    form_url = None
    success_url = None

    def get_form_url(self, request):
        return self.form_url

    def get_success_url(self, request):
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super(AjaxFormView, self).get_context_data(**kwargs)
        form_kwargs = self.get_form_kwargs(self.request)
        rendered_form_content = render_to_string(self.ajax_template, {"form" : self.form_class(**form_kwargs)})

        context.update({
            "form_url" : self.get_form_url(self.request),
            "success_url" : self.get_success_url(self.request),
            "rendered_form_content" : rendered_form_content
        })
        return context


class HomePageView(TemplateView):
    template_name = 'landing.html'


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        super(TemplateView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        # Delegate ajax request to DRF view
        if request.is_ajax():
            return ClassifiedViewSet.as_view({'get': 'list'})(request)

        return super(SearchView, self).get(request, *args, **kwargs)


class DetailView(TemplateView):
    template_name = 'search_detail.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'