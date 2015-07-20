from django.views.generic import TemplateView


__all__ = ['InspectionFormView']

class InspectionLoginView(TemplateView):
    template_name = 'inspection/inspection_login.html'

class InspectionListView(TemplateView):
    template_name = 'inspection/inspection_list.html'

class InspectionFormView(TemplateView):
    template_name = 'inspection/inspection_form.html'