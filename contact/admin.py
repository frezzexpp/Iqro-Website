from django.contrib import admin
from .models import *

# Contact register:
@admin.register(Contact)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'create_at')
    search_fields = ('create_at', )
    readonly_fields = (
        'create_at',
    )