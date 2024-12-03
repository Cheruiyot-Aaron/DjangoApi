from django.db import models
from django.contrib.auth.models import User

class WaterDispenser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="installations")
    location = models.CharField(max_length=255)
    installation_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Installed', 'Installed'), ('Pending', 'Pending')])
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Dispenser at {self.location} - {self.status}"

