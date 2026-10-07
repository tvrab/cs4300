"""
URL configuration for movie_theater_booking project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include bookings app routes at the root level
    path('', include('bookings.urls')),
]
