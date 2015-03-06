from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin

from core.models.user_models import User
from core.admin.user_admin import UserAdmin
from core.admin.admin_site import NoLemonAdminSite

from registration.admin import RegistrationAdmin
from registration.models import RegistrationProfile

admin.site = NoLemonAdminSite()

admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(RegistrationProfile)