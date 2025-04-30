from django.db import models
from django.contrib.auth.models import Core


class Appointments(models.Model):
    patient = models.ForeignKey(
        Core, on_delete=models.CASCADE, related_name="appointments"
    )
    date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Cita de {self.patient.username} el {self.date}"
