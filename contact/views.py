from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer
from core.utils import send_contact_autoreply
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

@method_decorator(ratelimit(key='ip', rate='5/h', method='POST', block=True), name='dispatch')
class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()
        try:
            send_contact_autoreply(contact)
        except Exception as e:
            print(f"Email failed: {e}")