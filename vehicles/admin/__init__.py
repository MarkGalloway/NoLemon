from django.contrib import admin

from core.admin import admin
from ..models import Vehicle, Make, Model, Trim, Body, Transmission, Fuel, BasicColour, Colour


# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Trim)
admin.site.register(Body)
admin.site.register(Transmission)
admin.site.register(Fuel)
admin.site.register(BasicColour)
admin.site.register(Colour)
