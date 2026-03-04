from django.contrib import admin
from .models import Module, PricingPlan

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'order']
    list_editable = ['order']

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'billing_cycle', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    filter_horizontal = ['modules']