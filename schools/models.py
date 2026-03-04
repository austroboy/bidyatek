from django.db import models
from django.utils.translation import gettext_lazy as _

class School(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='schools/logos/', blank=True, null=True)
    location = models.CharField(max_length=200)
    description_en = models.TextField(blank=True)
    description_bn = models.TextField(blank=True)
    testimonial_en = models.TextField(blank=True, help_text=_('Optional testimonial quote'))
    testimonial_bn = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    target_audience = models.CharField(
    max_length=200,help_text=_('e.g. Small schools'))

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name