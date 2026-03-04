from django.contrib import admin
from .models import School

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['name']