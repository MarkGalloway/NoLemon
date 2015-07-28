from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm


__all__ = ["BaseLoginForm"]


class BaseLoginForm(BaseAuthenticationForm):

    error_messages = {
        'invalid_login': "Invalid username or password.",
        'inactive': "This account is waiting for admin activation.",
    }