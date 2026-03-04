from django.db import models

class FAQ(models.Model):
    question_en = models.CharField(max_length=300)
    question_bn = models.CharField(max_length=300, blank=True)
    answer_en = models.TextField()
    answer_bn = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question_en