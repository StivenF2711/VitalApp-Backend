from django.test import TestCase
from django.contrib.auth.models import User
from .models import Appointments
from django.utils import timezone


class AppointmentModelTest(TestCase):
    def test_appointment_creation(self):
        user = User.objects.create_user(username="testuser", password="12345")
        appointment = Appointments.objects.create(
            patient=user, date=timezone.now(), reason="Dolor de cabeza"
        )
        self.assertEqual(appointment.patient.username, "testuser")
        self.assertEqual(appointment.reason, "Dolor de cabeza")
