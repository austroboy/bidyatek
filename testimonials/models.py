from django.db import models

class Testimonial(models.Model):
    author_name = models.CharField(max_length=200)
    school_name = models.CharField(max_length=200)
    content_en = models.TextField()
    content_bn = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.author_name} - {self.school_name}"