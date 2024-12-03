from rest_framework import serializers
from .models import WaterDispenser

class WaterDispenserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterDispenser
        fields = ['id', 'user', 'location', 'installation_date', 'status', 'notes']
