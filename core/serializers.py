from rest_framework import serializers
from .models import SiteSettings, PageSEO, HowItWorksStep, LiveCounter, NewsletterSubscriber
from core.utils import validate_recaptcha

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'


class PageSEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageSEO
        fields = '__all__'


class HowItWorksStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowItWorksStep
        fields = '__all__'


class LiveCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveCounter
        fields = '__all__'


class NewsletterSubscribeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    # recaptcha_token = serializers.CharField(write_only=True)

    def validate_recaptcha_token(self, value):
        if not validate_recaptcha(value):
            raise serializers.ValidationError('reCAPTCHA validation failed.')
        return value

    def create(self, validated_data):
        email = validated_data['email']
        subscriber, created = NewsletterSubscriber.objects.get_or_create(
            email=email,
            defaults={'active': True}
        )
        if not created and not subscriber.active:
            subscriber.active = True
            subscriber.save()
        return subscriber