""" URL routing configuration for the bookings app API endpoints. """ 

from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from .views import MovieViewSet, SeatViewSet, BookingViewSet 

# DefaultRouter automatically generates RESTful URLs for all ViewSet operations (GET, POST, PUT, DELETE) 
router = DefaultRouter() 
router.register(r'movies', MovieViewSet, basename='movie') 
router.register(r'seats', SeatViewSet, basename='seat') 
router.register(r'bookings', BookingViewSet, basename='booking') 

urlpatterns = [ 
    # Expose API endpoints under the api/ URL path prefix 
    path('api/', include(router.urls)),    
]