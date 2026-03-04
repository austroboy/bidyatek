from rest_framework import serializers
from .models import Module, PricingPlan

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class PricingPlanSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = PricingPlan
        fields = '__all__'