from rest_framework import serializers
from .models import DemoRequest
from core.utils import validate_recaptcha

class DemoRequestSerializer(serializers.ModelSerializer):
    recaptcha_token = serializers.CharField(write_only=True)

    class Meta:
        model = DemoRequest
        fields = '__all__'
        read_only_fields = ['status', 'created_at', 'updated_at']

    def validate_recaptcha_token(self, value):
        if not validate_recaptcha(value):
            raise serializers.ValidationError('reCAPTCHA validation failed.')
        return value