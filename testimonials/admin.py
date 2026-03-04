from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'school_name', 'rating', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['rating']