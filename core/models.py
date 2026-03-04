from django.db import models
from django.utils.translation import gettext_lazy as _

class SiteSettings(models.Model):
    """Singleton model for global site settings"""
    site_name = models.CharField(max_length=100, default='BIDYATek')
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    business_hours = models.CharField(max_length=200, blank=True, help_text=_('e.g. Sat-Thu, 9:00 AM - 6:00 PM'))
    facebook_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    whatsapp_number = models.CharField(max_length=20, blank=True, help_text=_('Include country code'))
    analytics_id = models.CharField(max_length=50, blank=True, help_text=_('Google Analytics 4 measurement ID'))
    video_embed_url = models.URLField(blank=True, help_text=_('YouTube or Vimeo embed URL for demo video'))
    newsletter_enabled = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Site Settings')
        verbose_name_plural = _('Site Settings')

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return self.site_name


class PageSEO(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('about', 'About'),
        ('features', 'Features'),
        ('pricing', 'Pricing'),
        ('contact', 'Contact'),
        ('blog', 'Blog'),
        ('faq', 'FAQ'),
        ('clients', 'Clients'),
    ]
    page = models.CharField(max_length=20, choices=PAGE_CHOICES, unique=True)
    meta_title_en = models.CharField(max_length=200, blank=True)
    meta_title_bn = models.CharField(max_length=200, blank=True)
    meta_description_en = models.TextField(max_length=500, blank=True)
    meta_description_bn = models.TextField(max_length=500, blank=True)
    og_image = models.ImageField(upload_to='seo/', blank=True, null=True)

    class Meta:
        verbose_name = _('Page SEO')
        verbose_name_plural = _('Page SEO')

    def __str__(self):
        return f"SEO for {self.get_page_display()}"


class HowItWorksStep(models.Model):
    title_en = models.CharField(max_length=200)
    title_bn = models.CharField(max_length=200, blank=True)
    description_en = models.TextField()
    description_bn = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = _('How It Works Step')
        verbose_name_plural = _('How It Works Steps')

    def __str__(self):
        return self.title_en


class LiveCounter(models.Model):
    label_en = models.CharField(max_length=100)
    label_bn = models.CharField(max_length=100, blank=True)
    value = models.PositiveIntegerField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = _('Live Counter')
        verbose_name_plural = _('Live Counters')

    def __str__(self):
        return f"{self.label_en}: {self.value}"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Newsletter Subscriber')
        verbose_name_plural = _('Newsletter Subscribers')

    def __str__(self):
        return self.email