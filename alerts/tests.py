from django.test import TestCase
from django.contrib.auth.models import User
from .models import Alert


class AlertModelTest(TestCase):
    def test_alert_creation(self):
        user = User.objects.create_user(username="alertuser", password="12345")
        alert = Alert.objects.create(
            patient=user, message="Tómate tu medicamento", is_read=False
        )
        self.assertEqual(alert.patient.username, "alertuser")
        self.assertEqual(alert.message, "Tómate tu medicamento")
        self.assertFalse(alert.is_read)
