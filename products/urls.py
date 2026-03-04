from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ModuleViewSet, PricingPlanViewSet

router = DefaultRouter()
router.register(r'modules', ModuleViewSet)
router.register(r'pricing-plans', PricingPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]