from django.db import models
from django.utils.translation import gettext_lazy as _

class Module(models.Model):
    name_en = models.CharField(max_length=100)
    name_bn = models.CharField(max_length=100, blank=True)
    description_en = models.TextField()
    description_bn = models.TextField(blank=True)
    tag_en = models.CharField(max_length=100, blank=True,default="")
    tag_bn = models.CharField(max_length=100, blank=True,default="")
    stat_en = models.CharField(max_length=100, blank=True,default="")
    stat_bn = models.CharField(max_length=100, blank=True,default="")
    icon = models.ImageField(upload_to='modules/icons/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name_en


class PricingPlan(models.Model):
    BILLING_CHOICES = [
        ('monthly', 'Monthly'),
        ('annual', 'Annual'),
    ]
    name = models.CharField(max_length=50)  # Basic, Standard, Enterprise
    target_audience = models.CharField(max_length=200, help_text=_('e.g. Small schools'))
    price = models.DecimalField(max_digits=10, decimal_places=2)
    billing_cycle = models.CharField(max_length=10, choices=BILLING_CHOICES, default='monthly')
    support_type = models.CharField(max_length=200, help_text=_('e.g. Email support'))
    school_size_limit = models.PositiveIntegerField(help_text=_('Maximum number of students'), blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    modules = models.ManyToManyField(Module, related_name='plans', blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.billing_cycle})"