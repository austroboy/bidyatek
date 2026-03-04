from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import DemoRequest
from .serializers import DemoRequestSerializer
from core.utils import send_demo_confirmation_email
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

@method_decorator(ratelimit(key='ip', rate='5/h', method='POST', block=True), name='dispatch')
class DemoRequestCreateView(generics.CreateAPIView):
    queryset = DemoRequest.objects.all()
    serializer_class = DemoRequestSerializer

    def perform_create(self, serializer):
        demo = serializer.save()
        # Send confirmation email
        try:
            send_demo_confirmation_email(demo)
        except Exception as e:
            # Log error but don't break the response
            print(f"Email failed: {e}")