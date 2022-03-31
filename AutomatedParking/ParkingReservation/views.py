from django.shortcuts import render
from .models import Reservation, Car, Parking


def home(request):
    return render(request, 'index.html', {})


def user_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations.html', {"reservations": reservations})
