from django.contrib import admin
from .models import Parking, Reservation, Car


# Register your models here.
admin.site.register(Parking)
admin.site.register(Reservation)
admin.site.register(Car)
