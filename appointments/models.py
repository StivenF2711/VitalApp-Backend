from django.db import models
from django.contrib.auth.models import User


class Appointments(models.Model):
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="appointments"
    )
    date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Cita de {self.patient.username} el {self.date}"
