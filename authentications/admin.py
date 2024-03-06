
# Register your models here.

# Register your models here.
from django.contrib import admin
from .models import User


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth',
                    'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'date_of_birth', 'password')}),
        ('Permissions', {'fields': ('is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'password1', 'password2'),
        }),
    )


admin.site.register(User, CustomUserAdmin)
