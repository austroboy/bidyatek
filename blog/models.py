from django.db import models
from django.utils.text import slugify

from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name_en = models.CharField(max_length=100, unique=True)
    name_bn = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name_en
    

class Tag(BaseModel):
    name_en = models.CharField(max_length=100,unique=True)
    name_bn = models.CharField(max_length=100,unique=True)

  
    def __str__(self):
        return self.name_en



class BlogPost(BaseModel):

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title_en = models.CharField(max_length=200)
    title_bn = models.CharField(max_length=200, blank=True)

    slug = models.SlugField(unique=True, blank=True)

    content_en = models.TextField()
    content_bn = models.TextField(blank=True)

    excerpt_en = models.TextField(blank=True)
    excerpt_bn = models.TextField(blank=True)


    author_en = models.CharField(max_length=100)
    author_bn = models.CharField(max_length=100, blank=True)

    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="blogs"
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="blogs"
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft"
    )

    is_published = models.BooleanField(default=True)

    published_date = models.DateTimeField(default=timezone.now)

   
    def generate_unique_slug(self):
        base_slug = slugify(self.title_en)
        slug = base_slug
        counter = 1

        while BlogPost.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        return slug

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = self.generate_unique_slug()

        if self.status == "published":
            self.is_published = True
            if not self.published_date:
                self.published_date = timezone.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en