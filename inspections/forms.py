from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from core.forms import BaseLoginForm, ErrorsOnFirstFieldMixin
from .models import Shop

__all__ = ["MechanicLoginForm"]

class MechanicLoginForm(ErrorsOnFirstFieldMixin, BaseLoginForm):

    def confirm_login_allowed(self, user):
        super(MechanicLoginForm, self).confirm_login_allowed(user)

        if (user.is_superuser):
            return

        # Prevent all users lacking a group that has been assigned to a shop from logging in
        shop_permissions = user.groups.exclude(shop__id__isnull=True).count()

        if (shop_permissions == 0):
            raise ValidationError(self.error_messages['invalid_login'])