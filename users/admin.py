from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUsers

class CustomUserAdmin(UserAdmin):
    # Admin panelda ko'rsatiladigan ustunlar
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)

    # Foydalanuvchi yaratish va tahrirlash formasi uchun maydonlar
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

# CustomUsers modelini admin panelda ro'yxatdan o'tkazamiz
admin.site.register(CustomUsers, CustomUserAdmin)
