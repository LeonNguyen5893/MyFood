from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import MyFoodUser


class MyFoodUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)})
    )

    search_fields = ('username', 'email')
    ordering = ('username', 'email')
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(MyFoodUser, MyFoodUserAdmin)

