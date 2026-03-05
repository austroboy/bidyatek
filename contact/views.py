from rest_framework import generics, status
from rest_framework.response import Response
from django_ratelimit.core import is_ratelimited

from .models import Contact
from .serializers import ContactSerializer
from core.utils import send_contact_autoreply


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        # Single clean rate limit check — increment=True counts this request
        limited = is_ratelimited(
            request,
            group='contact_create',
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
                    "message": "You can only send 5 messages per hour."
                },
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        contact = serializer.save()
        try:
            send_contact_autoreply(contact)
        except Exception as e:
            print(f"Email failed: {e}")

