# core/tests.py

from django.test import TestCase
from core.models import Core
from datetime import date

class CoreModelTest(TestCase):
    def test_core_creation(self):
        core = Core.objects.create(
            first_name="Juan",
            last_name="Pérez",
            birth_date=date(1990, 1, 1),
            gender="M",
            email="juan.perez@example.com",
            phone_number="1234567890",
            address="Calle Falsa 123"
        )

        self.assertEqual(core.first_name, "Juan")
        self.assertEqual(core.last_name, "Pérez")
        self.assertEqual(core.birth_date, date(1990, 1, 1))
        self.assertEqual(core.gender, "M")
        self.assertEqual(core.email, "juan.perez@example.com")
        self.assertEqual(core.phone_number, "1234567890")
        self.assertEqual(core.address, "Calle Falsa 123")

    def test_string_representation(self):
        core = Core.objects.create(
            first_name="Ana",
            last_name="Gómez",
            birth_date=date(1985, 5, 10),
            gender="F",
            email="ana.gomez@example.com"
        )

        self.assertEqual(str(core), "Ana Gómez")
