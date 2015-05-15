from django.contrib.auth.admin import UserAdmin as BaseAdmin

__all__ = ['UserAdmin']

class UserAdmin(BaseAdmin):
    
    # List View Attributes
    list_filter = []
    search_fields = []
    exclude = []
    inlines = []
    
    list_display = ('username', 'email', 'date_joined', 'is_staff')
    
    # Form View Attributes
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
    )