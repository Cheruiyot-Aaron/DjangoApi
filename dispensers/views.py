from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import WaterDispenser
from .serializers import WaterDispenserSerializer

class WaterDispenserViewSet(viewsets.ModelViewSet):
    queryset = WaterDispenser.objects.all()
    serializer_class = WaterDispenserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Associate the logged-in user with the installation
        serializer.save(user=self.request.user)
