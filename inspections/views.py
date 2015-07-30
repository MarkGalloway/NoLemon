from django.views import generic
from django.views import decorators
from django.utils.decorators import method_decorator
from django.contrib import auth
from django import shortcuts
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from core.views import AjaxFormMixin, AjaxValidateView, AjaxFormView
from .forms import *
from .models import *

__all__ = ['InitialView', 'InspectionLoginView', 'InspectionLogoutView',
           'InspectionListView', 'InitialAjax', 'VehicleMixin', 'VehicleAjax', 'VehicleFormView',
           'PhotosFormView', 'PhotosAjax', 'Test']


class MechanicLoginRequiredMixin(object):
    shops = []

    def dispatch(self, *args, **kwargs):

        # superusers can see all shops
        if self.request.user.is_superuser :
            self.shops = Shop.objects.all()
        else:
            # Prevent all users lacking a group that has been assigned to a shop from accessing this page
            self.shops = self.request.user.groups.exclude(shop__id__isnull=True)

        if (len(self.shops) == 0):
            return shortcuts.redirect('inspections:login')

        return super(MechanicLoginRequiredMixin, self).dispatch(*args, **kwargs)


class InspectionLoginView(generic.FormView):
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


class InspectionListView(MechanicLoginRequiredMixin, generic.ListView):
    template_name = 'inspection/inspection_list.html'
    paginate_by = 30
    paginate_orphans = 5
    search_kwarg = 's'
    order_kwarg = 'o'
    order_columns = ['id', 'customer__first_name', 'technician', 'date_completed',
                     '-id', '-customer__first_name', '-technician', '-date_completed']
    ordering = ['-date_completed']

    def get_queryset(self):
        self.queryset = Inspection.objects.select_related('customer__first_name', 'customer__last_name', 'customer__username')\
            .filter(shop__id__in = [shop.id for shop in self.shops])
        return super(InspectionListView, self).get_queryset()

    def get_ordering(self):
        column = self.request.GET.get(self.order_kwarg)

        if column is not None:
            try:
                column  = int(column)
            except ValueError:
                column  = None

        if column is not None:
            self.ordering = [self.order_columns[column]]

        return self.ordering

    def get_context_data(self, **kwargs):
        context = super(InspectionListView, self).get_context_data(**kwargs)

        context.update({
            'shops' : self.shops,
            'order_columns' : self.order_columns,
            'ordering' : self.ordering[0],
            'page_kwarg' : self.page_kwarg,
            'order_kwarg' : self.order_kwarg })

        return context


class InitialMixin(MechanicLoginRequiredMixin, AjaxFormMixin):
    ajax_template = 'inspection/initial.html'
    form_class = InitialForm

    def get_form_kwargs(self, request):
        return {'shops' : self.shops}


class InitialAjax(InitialMixin, AjaxValidateView):
    def get_form_kwargs(self, request):
        kwargs = super(InitialAjax, self).get_form_kwargs(request)

        id = request.POST.get('id')
        existing_inspection = Inspection.objects.filter(id=id, shop__in=[shop.id for shop in self.shops]).first()

        if (existing_inspection):
            kwargs.update({'instance' : existing_inspection})

        return kwargs


class InitialView(InitialMixin, AjaxFormView):
    template_name = 'inspection/initial_base.html'
    form_url = reverse_lazy('inspections:initial_ajax')
    success_url = reverse_lazy('inspections:vehicles')


class VehicleMixin(MechanicLoginRequiredMixin, AjaxFormMixin):
    ajax_template = 'inspection/vehicles.html'
    form_class = VehicleForm

    def get_form_kwargs(self, request):
        id = self.kwargs.get('id')
        self.inspection = shortcuts.get_object_or_404(Inspection, pk=id, shop_id__in=[shop.id for shop in self.shops])

        return {'inspection' : self.inspection,
            'instance' : self.inspection.vehicle}


class VehicleAjax(VehicleMixin, AjaxValidateView):
    pass


class VehicleFormView(VehicleMixin, AjaxFormView):
    template_name = 'inspection/vehicles_base.html'
    form_template_name = 'inspection/vehicles.html'
    success_url = reverse_lazy('inspections:list')

    def get_form_url(self, request):
        id = self.kwargs.get('id')
        return reverse_lazy('inspections:vehicle_ajax', kwargs={'id' : id})

    def get_success_url(self, request):
        id = self.kwargs.get('id')
        return reverse_lazy('inspections:photos', kwargs={'id' : id})


class PhotosMixin(MechanicLoginRequiredMixin, AjaxFormMixin):
    ajax_template = 'inspection/photos.html'
    form_class = PhotoForm

    def get_form_kwargs(self, request):
        id = self.kwargs.get('id')
        self.inspection = shortcuts.get_object_or_404(Inspection, pk=id, shop_id__in=[shop.id for shop in self.shops])
        return {'instance' : self.inspection}


class PhotosAjax(PhotosMixin, AjaxValidateView):
    pass


class PhotosFormView(PhotosMixin, AjaxFormView):
    template_name = 'inspection/photos_base.html'
    form_template_name = 'inspection/photos.html'
    success_url = reverse_lazy('inspections:list')

    def get_form_url(self, request):
        id = self.kwargs.get('id')
        return reverse_lazy('inspections:photos_ajax', kwargs={'id' : id})

    def get_success_url(self, request):
        return self.success_url


class Test(generic.FormView):
    template_name = 'inspection/inspection_form.html'
    form_class = InspectionForm
