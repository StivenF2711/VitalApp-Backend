from django.test import TestCase
from django.contrib.auth.models import User
from .models import Result  # ← el nombre correcto del modelo


class ResultModelTest(TestCase):
    def test_result_creation(self):
        user = User.objects.create_user(username="resultuser", password="12345")
        result = Result.objects.create(
            patient=user, test_name="Colesterol", result_value="Alto", date="2025-04-13"
        )
        self.assertEqual(result.patient.username, "resultuser")
        self.assertEqual(result.test_name, "Colesterol")
        self.assertEqual(result.result_value, "Alto")
        self.assertEqual(str(result.date), "2025-04-13")

    def test_string_representation(self):
        user = User.objects.create_user(username="resultuser", password="12345")
        result = Result.objects.create(
            patient=user, test_name="Colesterol", result_value="Alto", date="2025-04-13"
        )
        self.assertEqual(str(result), "Colesterol de resultuser - 2025-04-13")
