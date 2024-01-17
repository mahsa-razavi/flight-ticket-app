from django.shortcuts import render, redirect
from .models import Flight, Booking
from .forms import BookingForm
from django.contrib import messages

# Create your views here.
def search(request):
    if request.method == 'GET':
        source = request.GET.get('source')
        destination = request.GET.get('destination')
        date = request.GET.get('date')

        flights = Flight.objects.filter(departure_date=date, departure_airport=source, arrival_airport=destination)
        context = {'flights' : flights}
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')

def book_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.flight = flight
            flight.booked_seats += 1
            booking.seat_number = flight.booked_seats
            flight.save()
            booking.save()
            return redirect('booking_confirmation')
    else:
        form = BookingForm()

    context = {'form': form, 'flight': flight}
    return render(request, 'book_flight.html', context)

def booking_confirmation(request):
    return render(request, 'booking_confirmation.html')


def bookings(request):
    bookings = Booking.objects.all()
    context = {'bookings':bookings}
    return render(request, 'bookings.html', context)        