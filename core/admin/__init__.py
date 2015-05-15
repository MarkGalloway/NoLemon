from django.contrib import admin
import django.contrib.auth.models as auth_models
import django.contrib.auth.admin as auth_admin

from core.admin.admin_site import NoLemonAdminSite
from core.admin.user_admin import *
from core.admin.registration_admin import *

import core.models as core_models

admin.site = NoLemonAdminSite()

admin.site.register(core_models.user_models.User, user_admin.UserAdmin)
admin.site.register(core_models.registration_models.RegistrationProfile, registration_admin.RegistrationAdmin)



