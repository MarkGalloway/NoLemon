from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from registration import signals
from registration.forms import UserRegistrationForm
from registration.models import RegistrationProfile

class _RequestPassingFormView(FormView):
    """
    A version of FormView which passes extra arguments to certain methods,
    notably passing the HTTP request nearly everywhere, to enable finer-grained processing.
    """
    
    def get(self, request, *args, **kwargs):
        # Pass request to get_form_class and get_form for per-request
        # form control.
        form_class = self.get_form_class(request)
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        # Pass request to get_form_class and get_form for per-request
        # form control.
        form_class = self.get_form_class(request)
        form = self.get_form(form_class)
        if form.is_valid():
            # Pass request to form_valid.
            return self.form_valid(request, form)
        else:
            return self.form_invalid(form)

    def get_form_class(self, request=None):
        return super(_RequestPassingFormView, self).get_form_class()

    def get_form_kwargs(self, request=None, form_class=None):
        return super(_RequestPassingFormView, self).get_form_kwargs()

    def get_initial(self, request=None):
        return super(_RequestPassingFormView, self).get_initial()

    def get_success_url(self, request=None, user=None):
        # We need to be able to use the request and the new user when
        # constructing success_url.
        return super(_RequestPassingFormView, self).get_success_url()

    def form_valid(self, form, request=None):
        return super(_RequestPassingFormView, self).form_valid(form)

    def form_invalid(self, form, request=None):
        return super(_RequestPassingFormView, self).form_invalid(form)


class RegistrationView(_RequestPassingFormView):
    """
    A registration backend which follows a simple workflow:
    1. User signs up, inactive account is created.
    2. Email is sent to user with activation link.
    3. User clicks activation link, account is now active.
    Required:
    * The setting `ACCOUNT_ACTIVATION_DAYS` be supplied, specifying
      (as an integer) the number of days from registration during
      which a user may activate their account.
    * The creation of the templates
      `activation_email_subject.txt` and
      `activation_email.txt`, which will be used for
      the activation email. 
    """
    form_class = UserRegistrationForm
    http_method_names = ['get', 'post', 'head', 'options', 'trace']
    template_name = 'registration_form.html'

    def form_valid(self, request, form):
        new_user = self.register(request, **form.cleaned_data)
        success_url = self.get_success_url(request, new_user)
        
        # success_url may be a simple string, or a tuple providing the full argument set for redirect().
        # Attempting to unpack it tells us which one it is.
        try:
            to, args, kwargs = success_url
            return redirect(to, *args, **kwargs)
        except ValueError:
            return redirect(success_url)

    def register(self, request, **cleaned_data):
        """
        Given a username, email address and password, register a new
        user account, which will initially be inactive.
        * A new `User` object, and a new `registration.models.RegistrationProfile` will be created.
        * An email will be sent to the supplied email address; this email should contain an activation link. 
        * the signal `signals.user_registered` will be sent
        """
        
        username = cleaned_data['username']
        email = cleaned_data['email']
        password = cleaned_data['password1']
        extra_fields = {}

        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
            
        new_user = RegistrationProfile.objects.create_inactive_user(username, email, password, site, extra_fields)
        signals.user_registered.send(sender=self.__class__, user=new_user, request=request)
        return new_user
    
    def get_success_url(self, request, user):
        """
        Return the name of the URL to redirect to after successful user registration.
        """
        return ('registration_complete', (), {})
                
                      
class ActivationView(TemplateView):
    """
    User activation view.
    """
    http_method_names = ['get']
    template_name = 'activate.html'

    def get(self, request, *args, **kwargs):
        activated_user = self.activate(request, *args, **kwargs)
        
        if type(activated_user) is RegistrationProfile:
            error = None
            user = activated_user.user.username
        else:
            error = activated_user
            user = ''
            
        context = {'account' : activated_user, 'error' : error, 'user' : user}
        return render(request, self.template_name, context)

    def activate(self, request, activation_key):
        """
        Given an an activation key, look up and activate the user account corresponding to that key (if possible).
        After successful activation, the signal `signals.user_activated` will be sent, with the
        newly activated `User` as the keyword argument `user` and the class of this backend as the sender.
        """
        activated_user = RegistrationProfile.objects.activate_user(activation_key)
        if type(activated_user) is RegistrationProfile:
            signals.user_activated.send(sender=self.__class__, user=activated_user, request=request)
        return activated_user