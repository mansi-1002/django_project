from django.test import TestCase
from .models import Reservation
from datetime import datetime

class ReservationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up test data
        cls.reservation = Reservation.objects.create(
            first_name="John",
            last_name="Doe"
        )

    def test_fields(self):
        # Test if fields are of the correct type
        self.assertIsInstance(self.reservation.first_name, str)
        self.assertIsInstance(self.reservation.last_name, str)

    def test_timestamps(self):
        # Test if booking_time is an instance of datetime
        self.assertIsInstance(self.reservation.booking_time, datetime)