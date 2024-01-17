from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_number = models.IntegerField()
    airlines = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    departure_airport = models.CharField(max_length=100)
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    arrival_airport = models.CharField(max_length=100)
    max_seat = models.IntegerField(default=60)
    booked_seats = models.IntegerField()
    price = models.IntegerField(null=True)

class Airlines(models.Model):
    airlines_id = models.IntegerField()
    airlines_name = models.CharField(max_length=50)
    airlines_phone = models.CharField(max_length=20)

class Airport(models.Model):
    airport_id = models.IntegerField()
    airport_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

class Booking(models.Model):
    flight = models.ForeignKey("Flight", on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=50)
    passenger_email = models.EmailField()
    passenger_phone = models.CharField(max_length=20, null=True)
    passenger_age = models.IntegerField(null=True)
    seat_number = models.IntegerField()
    booking_date = models.DateField(auto_now_add=True)
