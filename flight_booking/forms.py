from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):

    class Meta():
        model = Booking
        fields = ['passenger_name', 'passenger_email', 'passenger_phone', 'passenger_age']
