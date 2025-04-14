from django.db import models
from django.contrib.auth.models import User


class Result(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Result")
    test_name = models.CharField(max_length=100)
    result_value = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.test_name} de {self.patient.username} - {self.date}"
