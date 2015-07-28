from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin

from ..models import User, RegistrationProfile
from .admin_site import *
from .user_admin import *
from .registration_admin import *

admin.site = NoLemonAdminSite()

admin.site.register(User, UserAdmin)
admin.site.register(RegistrationProfile, RegistrationAdmin)
admin.site.register(Group, GroupAdmin)

