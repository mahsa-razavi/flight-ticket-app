from django.urls import path
from . import views

urlpatterns = [
    path('search', views.search, name="search"),
    path('book_flight/<int:flight_id>/', views.book_flight, name="book_flight"),
    path('bookings', views.bookings, name="bookings"),
    path('booking_confirmation', views.booking_confirmation, name="booking_confirmation"),
]
