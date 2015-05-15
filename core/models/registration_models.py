import datetime
import hashlib
import random
import re

import django.utils.timezone as timezone
from django.conf import settings
from django.db import models
from django.db import transaction
from django.template.loader import render_to_string

from core.models import User

__all__ = ['RegistrationManager', 'RegistrationProfile']

class RegistrationManager(models.Manager):
    """
    Custom manager for the ``RegistrationProfile`` model.

    The methods defined here provide shortcuts for account creation and activation,
    including generation and emailing of activation keys, and for cleaning out expired inactive accounts.
    """

    def activate_user(self, activation_key):
        """
        Validate an activation key and activate the corresponding `User` if valid.

        If the key is valid and has not expired, return the `User` after activating.
        If the key is not valid or has expired, return `False`.
        If the key is valid but the `User` is already active return `False`.

        To prevent reactivation of an account which has been deactivated by site administrators, the activation key is
        reset to the string constant `RegistrationProfile.ACTIVATED` after successful activation.
        """

        errors = {
            'invalid-activation-key' : 'Activation key is invalid.',
            'no-registration' : 'No pending registration found. This account may already be active.',
            'key-expired' : 'Activation key has expired please re-register.'
        }

        if not re.compile('^[a-f0-9]{40}$').search(activation_key):
            return errors['invalid-activation-key']

        try:
            profile = self.get(activation_key=activation_key)
        except self.model.DoesNotExist:
            return errors['no-registration']

        if profile.activation_key_expired():
            return errors['key-expired']

        user = profile.user
        user.is_active = True
        user.save()

        profile.activation_key = self.model.ACTIVATED
        profile.save()

        return profile

    def create_inactive_user(self, username, email, password, site, extra_fields, send_email=True):
        """
        Create a new, inactive `User`, generate a `RegistrationProfile`
        and email its activation key to the `User`, returning the new `User`.
        By default, an activation email will be sent to the new user.
        """
        
        new_user = user_models.User.objects.create_user(username, email, password, **extra_fields)
        new_user.is_active = False
        new_user.save()

        registration_profile = self.create_profile(new_user)

        if send_email:
            registration_profile.send_activation_email(site)

        return new_user
    create_inactive_user = transaction.atomic(create_inactive_user)

    def create_profile(self, user):
        """
        Create a `RegistrationProfile` for a given `User`, and return the `RegistrationProfile`.

        The activation key for the `RegistrationProfile` will be a SHA1 hash,
        generated from a combination of the `User`'s username and a random salt.
        """
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        salted_username = salt + user.username
        activation_key = hashlib.sha1(salted_username.encode('utf-8')).hexdigest()

        return self.create(user=user, activation_key=activation_key)

    def delete_expired_user(self):
        """
        Remove expired instances of `RegistrationProfile` and their associated `User`s.

        Accounts to be deleted are identified by searching for instances of `RegistrationProfile` with expired activation
        keys, and then checking to see if their associated `User` instances have the field `is_active` set to `False`;
        any `User` who is both inactive and has an expired activation key will be deleted.

        `manage.py cleanupregistration`

        If you have a troublesome `User` and wish to disable their account while keeping it in the database,
        simply delete the associated `RegistrationProfile`.
        """
        
        for profile in self.all():
            try:
                if profile.activation_key_expired():
                    user = profile.user
                    if not user.is_active:
                        user.delete()
                        profile.delete()
            except user_models.User.DoesNotExist:
                profile.delete()


class RegistrationProfile(models.Model):
    """
    A simple profile which stores an activation key for use during user account registration.
    """

    ACTIVATED = "ALREADY_ACTIVATED"
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name='user')
    activation_key = models.CharField(max_length=40)
    objects = RegistrationManager()

    class Meta:
        app_label = 'auth'
        verbose_name = 'registration'
        verbose_name_plural = 'Site Registration'

    def __str__(self):
        return "Registration information for {}".format(self.user)

    def activation_key_expired(self):
        """
        Determine whether this `RegistrationProfile`'s activation key has expired.
        Returns: `True` if the key has expired.

        Key expiration is determined by a two-step process:
        1.  If the user has already activated, the key will have been reset to the string constant `ACTIVATED`.
            So the activation key should be expired.
        2.  Otherwise, the date the user signed up is incremented by the number of days specified in the setting `ACCOUNT_ACTIVATION_DAYS`
            If the result is less than or equal to the current date, the key has expired.
        """

        expiration_date = datetime.timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
        return self.activation_key == self.ACTIVATED or (self.user.date_joined + expiration_date <= timezone.now())
    activation_key_expired.boolean = True

    def send_activation_email(self, site):
        """
        Send an activation email to the user associated with this `RegistrationProfile`.

        The activation email will make use of two templates:
            - `activation_email_subject.txt`
            - `activation_email.txt`
        These templates will each receive the following context
        variables:
        `activation_key`: the activation key for the new account.
        `expiration_days`: The number of days remaining during which the account may be activated.
        `site`: An object representing the site on which the user registered;
                depending on whether ``django.contrib.sites`` is installed, this may be an instance of either
                `django.contrib.sites.models.Site` or `django.contrib.sites.models.RequestSite`
        """
        context = {
            'activation_key': self.activation_key,
            'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
            'site': site,
            'username': self.user.username,
        }

        subject = render_to_string('activation_email_subject.txt', context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        message = render_to_string('activation_email.txt', context)
        self.user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
