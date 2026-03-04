from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import DemoRequest

@admin.register(DemoRequest)
class DemoRequestAdmin(ImportExportModelAdmin):
    list_display = ['school_name', 'contact_person', 'email', 'status', 'created_at']
    list_filter = ['status', 'preferred_institute_type']
    search_fields = ['school_name', 'contact_person', 'email']
    list_editable = ['status']
    actions = ['export_as_csv']
    readonly_fields = ['created_at', 'updated_at']

    def export_as_csv(self, request, queryset):
        # Use import-export
        pass
    export_as_csv.short_description = "Export selected to CSV"