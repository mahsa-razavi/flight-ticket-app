from django.contrib import admin
from.models import Flight, Airlines, Airport, Booking

# Register your models here.
admin.site.register(Flight)
admin.site.register(Airlines)
admin.site.register(Airport)
admin.site.register(Booking)