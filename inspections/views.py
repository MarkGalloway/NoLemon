from django.views import generic
from django.views import decorators
from django.utils.decorators import method_decorator
from django.contrib import auth
from django import http
from django.utils.http import is_safe_url
from django import shortcuts
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages

from .forms import *

__all__ = ['InspectionFormView', 'InspectionLoginView', 'InspectionLogoutView', 'InspectionListView']


class MechanicLoginRequiredMixin(object):

    def dispatch(self, *args, login_url='inspections:list', **kwargs):
        if (self.request.user.shop_id is None):
            return shortcuts.redirect('inspections:login')
        return super(MechanicLoginRequiredMixin, self).dispatch(*args, **kwargs)

class InspectionLoginView(generic.FormView, MechanicLoginRequiredMixin):
    template_name = 'inspection/inspection_login.html'
    form_class = MechanicLoginForm
    login_redirect = 'inspections:list'

    @method_decorator(decorators.debug.sensitive_post_parameters())
    @method_decorator(decorators.csrf.csrf_protect)
    @method_decorator(decorators.cache.never_cache)
    def dispatch(self, *args, **kwargs):
        return super(InspectionLoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return shortcuts.redirect(self.login_redirect)

    def set_test_cookie(self):
        self.request.session.set_test_cookie()

    def check_and_delete_test_cookie(self):
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
            return True
        return False

    def get(self, request, *args, **kwargs):
        self.set_test_cookie()
        return super(InspectionLoginView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.check_and_delete_test_cookie()
            return self.form_valid(form)
        else:
            self.set_test_cookie()
            return self.form_invalid(form)

class InspectionLogoutView(generic.RedirectView):
    permanent = True
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, "Successfully logged out.")
        return super(InspectionLogoutView, self).get(request, *args, **kwargs)

    def get_redirect_url(self, **kwargs):
        return shortcuts.resolve_url('inspections:login')

class InspectionListView(generic.TemplateView):
    template_name = 'inspection/inspection_list.html'

class InspectionFormView(generic.TemplateView):
    template_name = 'inspection/inspection_form.html'

