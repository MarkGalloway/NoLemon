from core.admin import admin
from inspections.models import *
from django import forms


class InspectionCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_redeemed')
    exclude = ('redeemed_on',)
    readonly_fields = ('date_redeemed',)

    def date_redeemed(self, obj):
        if obj.redeemed_on:
            return obj.redeemed_on
        return 'N/A'


admin.site.register(Inspection)
admin.site.register(Shop)
admin.site.register(InspectionCode, InspectionCodeAdmin)