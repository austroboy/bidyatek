import requests
from django.conf import settings

def validate_recaptcha(token):
    """Validate Google reCAPTCHA v3 token"""
    if not settings.RECAPTCHA_SECRET_KEY:
        return True  # Bypass if not configured (development)
    
    payload = {
        'secret': settings.RECAPTCHA_SECRET_KEY,
        'response': token
    }
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
    result = response.json()
    return result.get('success', False) and result.get('score', 0) > 0.5


def send_demo_confirmation_email(demo_request):
    """Send confirmation email after demo request"""
    from django.core.mail import send_mail
    from django.template.loader import render_to_string
    from django.conf import settings
    
    subject = 'Thank you for requesting a demo - BIDYATek'
    html_message = render_to_string('emails/demo_confirmation.html', {'demo': demo_request})
    plain_message = f"Dear {demo_request.contact_person},\n\nThank you for requesting a demo of BIDYATek. We will contact you within 24 hours.\n\nRegards,\nBIDYATek Team"
    
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [demo_request.email],
        html_message=html_message,
        fail_silently=False,
    )


def send_contact_autoreply(contact):
    """Send auto-reply for contact form"""
    from django.core.mail import send_mail
    from django.conf import settings
    
    subject = 'Thank you for contacting BIDYATek'
    message = f"Dear {contact.name},\n\nThank you for reaching out to us. We have received your message and will get back to you soon.\n\nRegards,\nBIDYATek Team"
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [contact.email],
        fail_silently=False,
    )