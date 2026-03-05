from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import DemoRequest
from .serializers import DemoRequestSerializer
from core.utils import send_demo_confirmation_email
from django_ratelimit.core import is_ratelimited


class DemoRequestCreateView(generics.CreateAPIView):
    queryset = DemoRequest.objects.all()
    serializer_class = DemoRequestSerializer

    def create(self, request, *args, **kwargs):
        limited = is_ratelimited(
            request,
            group='demo_create',
            fn=self.create,
            key='ip',
            rate='5/h',
            method='POST',
            increment=True,
        )

        if limited:
            return Response(
                {
                    "error": "Too many requests",
                    "message": "You can only send 5 demo requests per hour."
                },
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        demo = serializer.save()
        try:
            send_demo_confirmation_email(demo)
        except Exception as e:
            print(f"Email failed: {e}")

