"""
Models for the Movie Theater Booking application.

This module defines the database schema for managing movies, seat availability, 
and customer reservations using the Django ORM.
"""

from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    """
    Represents a film available for viewing in the theater.

    Attributes: 
        title (CharField): The official title of the movie.
        description (TextField): Detailed plot summary or synopsis.
        release_date (DateField): The official release date.
        duration (IntegerField): Total runtime in minutes.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    
    def __str__(self):
        """ Return a user-friendly string representation of the movie. """
        return f"{self.title} ({self.duration} mins)"

class Seat(models.Model):
    """ Represents an individual physical seat within the theater.

    Attributes:
        seat_number (CharField): Unique seat identifier (like 'A1', '102', etc)
        is_booked (BooleanField): Flag indicating if the seat is currently reserved.
    """
    # Enforces unique seat numbers across the theater to prevent the same seat from being booked by more than one person
    seat_number = models.CharField(max_length=10, unique=True)

    # Seats start as available by default
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        """ Return seat identifier and current availability status. """
        status = "Booked" if self.is_booked else "Available"
        return f"Seat {self.seat_number} - {status}"

class Booking(models.Model):
    """
    Represents a seat reservation made by a registered user for a movie.

    Attributes:
        movie (ForeignKey): Reference to the Movie being booked.
        seat (ForeignKey): Reference to the Django User making the reservation.
        booking_date (DateTimeField): Auto-generated timestamp of reservation.
    """

    # CASCADE deletes linked bookings if the referenced movie/seat/user is removed
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.CharField(max_length=100) 

    # Automatically records the current date/time when a booking record is first created
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return a formatted summary string of the booking record."""
        return f"Booking for: {self.user} - {self.movie.title} (Seat {self.seat.seat_number})"