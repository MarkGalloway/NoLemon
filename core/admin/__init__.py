from django.contrib import admin

from ..models import User, RegistrationProfile
from .admin_site import *
from .user_admin import *
from .registration_admin import *

admin.site = NoLemonAdminSite()

admin.site.register(User, user_admin.UserAdmin)
admin.site.register(RegistrationProfile, registration_admin.RegistrationAdmin)
