""" 
Views and API ViewSets for the Movie Theater Booking application. 
Provides RESTful API endpoints for Movie, Seat, and Booking resources. 
""" 
from rest_framework import viewsets 
from .models import Movie, Seat, Booking 
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer 

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