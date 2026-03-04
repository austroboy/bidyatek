from django.db import models

class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('dashboard', 'Dashboard'),
        ('student_panel', 'Student Panel'),
        ('teacher_panel', 'Teacher Panel'),
        ('mobile_app', 'Mobile App'),
        ('website_template', 'Website Template'),
    ]
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='dashboard')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title