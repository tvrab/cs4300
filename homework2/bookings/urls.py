""" 
URL routing configuration for the bookings app API endpoints. 
Maps REST API endpoints and HTML web page template views.
""" 

from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from . import views

# DefaultRouter automatically generates RESTful URLs for all ViewSet operations (GET, POST, PUT, DELETE) 
router = DefaultRouter() 
router.register(r'movies', views.MovieViewSet, basename='movie') 
router.register(r'seats', views.SeatViewSet, basename='seat') 
router.register(r'bookings', views.BookingViewSet, basename='booking') 

urlpatterns = [ 
    # REST API endpoints
    path('api/', include(router.urls)),    

    # HTML web page routes for brower rendering
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/select-seats/', views.seat_booking, name='seat_booking'),
    path('booking-history/', views.booking_history, name='booking_history'),
]