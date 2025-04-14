from django.db import models
from django.contrib.auth.models import User


class Alert(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alerts")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Alerta para {self.patient.username} - {'Leída' if self.is_read else 'No leída'}"
