from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at']