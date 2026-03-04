from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question_en', 'order', 'is_active']
    list_editable = ['order', 'is_active']