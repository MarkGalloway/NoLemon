from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from core.admin import admin
from ..models import Vehicle, Make, Model, Trim, Body, Transmission, Fuel, BasicColour, Colour


# Register your models here.
admin.site.register(Vehicle, SimpleHistoryAdmin)
admin.site.register(Make, SimpleHistoryAdmin)
admin.site.register(Model, SimpleHistoryAdmin)
admin.site.register(Trim, SimpleHistoryAdmin)
admin.site.register(Body, SimpleHistoryAdmin)
admin.site.register(Transmission, SimpleHistoryAdmin)
admin.site.register(Fuel, SimpleHistoryAdmin)
admin.site.register(BasicColour, SimpleHistoryAdmin)
admin.site.register(Colour, SimpleHistoryAdmin)
