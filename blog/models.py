from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title_en = models.CharField(max_length=200)
    title_bn = models.CharField(max_length=200, blank=True)
    content_en = models.TextField()
    content_bn = models.TextField(blank=True)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en