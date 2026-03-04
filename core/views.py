from rest_framework import generics, viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from .models import SiteSettings, PageSEO, HowItWorksStep, LiveCounter, NewsletterSubscriber
from .serializers import (
    SiteSettingsSerializer, PageSEOSerializer,
    HowItWorksStepSerializer, LiveCounterSerializer,
    NewsletterSubscribeSerializer
)
from core.utils import send_demo_confirmation_email, send_contact_autoreply

class SiteSettingsView(generics.RetrieveAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer

    def get_object(self):
        return SiteSettings.get_settings()


class PageSEOViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PageSEO.objects.all()
    serializer_class = PageSEOSerializer
    lookup_field = 'page'


class HowItWorksStepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HowItWorksStep.objects.all()
    serializer_class = HowItWorksStepSerializer


class LiveCounterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LiveCounter.objects.all()
    serializer_class = LiveCounterSerializer


class NewsletterSubscribeView(generics.CreateAPIView):
    serializer_class = NewsletterSubscribeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': 'Subscribed successfully'}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()