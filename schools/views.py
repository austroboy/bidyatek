from rest_framework import viewsets
from .models import School
from .serializers import SchoolSerializer

class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = School.objects.filter(is_active=True)
    serializer_class = SchoolSerializer