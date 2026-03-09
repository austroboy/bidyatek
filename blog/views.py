from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.select_related('category').prefetch_related('tags').filter(is_published=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'

