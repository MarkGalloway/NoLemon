from django.conf import settings
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()

class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new user account.
    Validates that the requested username and email is not already in use, and
    requires the password to be entered twice to catch typos.
    """
    
    error_messages = {
        'duplicate_username': "*user already exists",
        'duplicate_email' : "*email already in use",
        'password_mismatch': "*passwords fields don't match",
    }

    password2 = forms.CharField(widget=forms.PasswordInput, label="Password (again)")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean_username(self):
        """
        Validate that the username is not already in use.
        """
        username = self.cleaned_data.get(name__iexact="username")
        if User._default_manager.filter(username=username):
            raise forms.ValidationError(self.error_messages['duplicate_username'])
        
        return username
    
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the site.
        """
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(self.error_messages['duplicate_email'])
        return email.tolower()

    def clean_password(self):
        """
        Verifiy that the values entered into the two password fields match.
        """
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2:
            if password != password2:
                raise forms.ValidationError(self.error_messages['password_mismatch'])
        return password