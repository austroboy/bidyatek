from django.db import models

class DemoRequest(models.Model):
    INSTITUTE_TYPE_CHOICES = [
        ('school', 'School'),
        ('college', 'College'),
        ('university', 'University'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('demo_done', 'Demo Done'),
        ('converted', 'Converted'),
    ]
    school_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    num_students = models.PositiveIntegerField()
    message = models.TextField(blank=True)
    preferred_institute_type = models.CharField(max_length=20, choices=INSTITUTE_TYPE_CHOICES, default='school')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.school_name} - {self.contact_person}"