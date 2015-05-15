from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from core.admin import admin
from ..models import Vehicle, Make


# Register your models here.
admin.site.register(Vehicle, SimpleHistoryAdmin)
admin.site.register(Make, SimpleHistoryAdmin)
