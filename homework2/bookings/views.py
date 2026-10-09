""" 
View definitions for the bookings application.

Contains both DRF ViewSets for the REST API and standard Django view functions
for rendering HTML templates (MVT pattern).
""" 
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets 
from .models import Movie, Seat, Booking 
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer 

# -------------------REST API ViewSets-------------------------------------------------

class MovieViewSet(viewsets.ModelViewSet): 
    """ API endpoint that allows movies to be viewed or edited. """ 
    
    queryset = Movie.objects.all() 
    serializer_class = MovieSerializer 

class SeatViewSet(viewsets.ModelViewSet): 
    """ API endpoint that allows seats to be viewed or edited. """ 
    
    queryset = Seat.objects.all() 
    serializer_class = SeatSerializer 
    
class BookingViewSet(viewsets.ModelViewSet): 
    """ API endpoint that allows bookings to be viewed or created. """ 
    
    queryset = Booking.objects.all() 
    serializer_class = BookingSerializer 
    
    def perform_create(self, serializer): 
        """ Save the booking and automatically mark the reserved seat as booked. """ 
        
        booking = serializer.save() 
        
        # Update seat status immediately so the seat cannot be double-booked 
        seat = booking.seat 
        seat.is_booked = True 
        seat.save()

# -------------------HTML Template Views --------------------------------------------
def movie_list(request):
    """
    Renders the homepage displaying all available movies.
    """
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


def seat_booking(request, movie_id):
    """
    Renders the seat selection form for a specific movie and handles reservation submissions.
    """
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all()

    # Get seat ids for seats already booked for this specific movie
    booked_seat_ids = Booking.objects.filter(movie=movie).values_list('seat_id', flat=True)

    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        user_name = request.POST.get('user_name')

        seat = get_object_or_404(Seat, id=seat_id)

        # Check if seat is already booked for this movie
        if int(seat_id) not in booked_seat_ids:
            # Create booking and mark seat as booked
            Booking.objects.create(
                movie=movie,
                seat=seat,
                user=user_name,
            )
            return redirect('booking_history')

    # Attach per-movie booking status to each seat for the template
    for seat in seats:
        seat.is_booked_for_movie = seat.id in booked_seat_ids

    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': seats
    })


def booking_history(request):
    """
    Renders the page displaying all past ticket bookings.
    """
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
