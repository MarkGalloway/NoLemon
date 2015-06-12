from django.core.mail import send_mail
from django.core import validators
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

__all__ = ['User']


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('username', max_length=30, unique=True,
        help_text= 'Required. 30 characters or fewer. Letters, digits and ./_ only.',
        validators=[
            validators.RegexValidator(r'^[\w.]+$', '*invalid characters', 'invalid')
        ])

    email = models.EmailField('email address', blank=False, unique=True)

    first_name = models.CharField('first name', max_length=30, blank=True)

    last_name = models.CharField('last name', max_length=30, blank=True)

    is_staff = models.BooleanField('admin status', default=False,
        help_text='Gives admin access to the site.')

    is_active = models.BooleanField('active', default=True,
        help_text='Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')

    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        If no names have been configured, displays the username.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        if not full_name.isspace():
            return full_name.strip()
        return self.username

    def get_short_name(self):
        "Returns the short name for the user."
        first_name = "%s" % (self.first_name)
        if first_name and not first_name.isspace():
            return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
