from rest_framework import viewsets
from .models import Module, PricingPlan
from .serializers import ModuleSerializer, PricingPlanSerializer

class ModuleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class PricingPlanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PricingPlan.objects.filter(is_active=True)
    serializer_class = PricingPlanSerializer