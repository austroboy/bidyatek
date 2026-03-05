from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SiteSettingsView, PageSEOViewSet, HowItWorksStepViewSet,
    LiveCounterViewSet, NewsletterSubscribeView
)

router = DefaultRouter()
router.register(r'page-seo', PageSEOViewSet)
router.register(r'how-it-works', HowItWorksStepViewSet)
router.register(r'live-counters', LiveCounterViewSet)

urlpatterns = [
    path('site-settings/', SiteSettingsView.as_view(), name='site-settings'),
    path('newsletter/subscribe/', NewsletterSubscribeView.as_view(), name='newsletter-subscribe'),
    path('', include(router.urls)),
    
]