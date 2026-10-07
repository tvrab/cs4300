"""
Unit and API Integration Tests for the Bookings Application.

Tests database model logic, string representations, DRF
serializer validation, and REST API endpoint status codes.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Movie, Seat, Booking

class MovieModelTest(TestCase):
    """
    Test suite for the Movie model and its methods
    """
    def setUp(self):
        """ Set up test data for Movie model tests. """

        self.movie = Movie.objects.create(
            title="Catch and Release",
            description="A woman struggles to rebuild her life after the sudden death of her fiance.",
            release_date="2006-10-20",
            duration=124,
        )

    def test_movie_creation(self):
        """ Verify that a Movie instance is created with correct attributes."""
        self.assertEqual(self.movie.title, "Catch and Release")
        self.assertEqual(self.movie.duration, 124)

    def test_movie_str_representation(self):
        """Verify the __str__ output formatting for Movie objects."""
        expected_str = "Catch and Release (124 mins)"
        self.assertEqual(str(self.movie), expected_str)

class SeatModelTest(TestCase):
    """
    Test suite for the Seat model and availability status.
    """

    def setUp(self):
        """Set up sample seat instances for testing."""
        self.seat_available = Seat.objects.create(seat_number="A1", is_booked=False)
        self.seat_booked = Seat.objects.create(seat_number="A2", is_booked=True)

    def test_seat_str_representation_paramaterized(self):
        """Verify __str__ formatting across both available and booked seat statuses."""

        test_cases = [
            (self.seat_available, "Seat A1 - Available"),
            (self.seat_booked, "Seat A2 - Booked"),
             
        ]

        # Loop through paramaterized test scenarios to verify string representation
        for seat, expected_str in test_cases:
            with self.subTest(seat=seat.seat_number):
                self.assertEqual(str(seat), expected_str)

class BookingAPITest(TestCase):
    """ 
    Integration test suite verifying REST API endpoints for Movie, Seat, and Booking resources.
    """

    def setUp(self):
        """Set up test environment with client, user, movie, and seats."""

        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.movie = Movie.objects.create(
            title="Catch and Release",
            description="A woman struggles to rebuild her life after the sudden death of her fiance.",
            release_date="2006-10-20",
            duration=124,
        )

        self.seat = Seat.objects.create(seat_number="B5", is_booked=False)

    def test_get_movies_api_endpoint(self):
        """Verify GET request to /api/movies/ returns HTTP 200 OK."""

        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_booking_api_success(self):
        """Verify successful POST request to create a valid booking updates seat status."""

        payload = {
            'movie': self.movie.id,
            'seat': self.seat.id,
            'user': self.user.id
        }

        response = self.client.post('/api/bookings/', payload, format='json')

        # Verify HTTP 201 Created status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify seat status automatically flipped to booked
        self.seat.refresh_from_db()
        self.assertTrue(self.seat.is_booked)

    def test_prevent_double_booking_validation(self):
        """
        Verify API returns HTTP 400 Bad Request when attempting
        to book an already reserved seat. 
        """

        # Pre-book seat B5
        self.seat.is_booked = True
        self.seat.save()

        payload = {
            'movie': self.movie.id,
            'seat': self.seat.id,
            'user': self.user.id,
        }

        response = self.client.post('/api/bookings/', payload, format='json')

        # Expect 400 Bad Request due to serializer validation
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)