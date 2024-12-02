from django.contrib import admin
from django.contrib import admin
from homepage.models import Service, Ideas, ProcessStep

# Service register:
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptions')
    search_fields = ('title',)


# Ideas register:
@admin.register(Ideas)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    search_fields = ('name',)


# Process register:
@admin.register(ProcessStep)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptions')
    search_fields = ('title',)