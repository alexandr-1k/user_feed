from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'first_name',)
    list_filter = ('email', 'first_name', 'last_name')
    ordering = ('-created_at',)
    list_display = ('email', 'first_name', 'last_name',
                    'is_active', 'is_staff')
    fieldsets = (
        ('General', {'fields': ('email', 'first_name', 'second_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        ('General', {
            'fields': ('email', 'first_name', 'last_name',  'password1',
                       'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(CustomUser, UserAdminConfig)
