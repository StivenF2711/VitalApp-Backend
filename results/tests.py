from core.models import Core
from results.models import Result
from django.test import TestCase

class ResultModelTest(TestCase):
    def test_result_creation(self):
        # Crear un objeto Core directamente
        core = Core.objects.create(
            first_name="Juan",
            last_name="Perez",
            birth_date="1990-01-01",
            gender="M",
            email="juan.perez@example.com",
            phone_number="123456789",
            address="Calle Ficticia 123"
        )

        # Crear el resultado y asignar el objeto Core como paciente
        result = Result.objects.create(
            patient=core,
            test_name="Colesterol",
            result_value="Alto",
            date="2025-04-13"
        )

        # Verifica que el resultado se creó correctamente
        self.assertEqual(result.patient.first_name, "Juan")
        self.assertEqual(result.patient.last_name, "Perez")
        self.assertEqual(result.patient.email, "juan.perez@example.com")
        self.assertEqual(result.test_name, "Colesterol")
        self.assertEqual(result.result_value, "Alto")
        self.assertEqual(str(result.date), "2025-04-13")

    def test_string_representation(self):
        # Crear un objeto Core directamente
        core = Core.objects.create(
            first_name="Juan",
            last_name="Perez",
            birth_date="1990-01-01",
            gender="M",
            email="juan.perez@example.com",
            phone_number="123456789",
            address="Calle Ficticia 123"
        )

        # Crear el resultado
        result = Result.objects.create(
            patient=core,
            test_name="Colesterol",
            result_value="Alto",
            date="2025-04-13"
        )

        self.assertEqual(str(result), "Colesterol de Juan Perez - 2025-04-13")
