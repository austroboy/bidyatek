from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import SiteSettings, PageSEO, HowItWorksStep, LiveCounter, NewsletterSubscriber

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()

@admin.register(PageSEO)
class PageSEOAdmin(admin.ModelAdmin):
    list_display = ['page', 'meta_title_en']

@admin.register(HowItWorksStep)
class HowItWorksStepAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'order']
    list_editable = ['order']

@admin.register(LiveCounter)
class LiveCounterAdmin(admin.ModelAdmin):
    list_display = ['label_en', 'value', 'order']
    list_editable = ['order']

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(ImportExportModelAdmin):
    list_display = ['email', 'subscribed_at', 'active']
    list_filter = ['active']
    search_fields = ['email']
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        # Use import-export or custom CSV
        pass
    export_as_csv.short_description = "Export selected to CSV"