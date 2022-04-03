from django.shortcuts import render
from .models import Reservation, Car, Parking
from .form import ReservationForm, CarForm
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'index.html', {})


def user_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations.html', {"reservations": reservations})


def add_reservations(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.price = 555  # TODO: fix this ASAP! This price should come from parking object.
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/reservations')
    else:
        form = ReservationForm
    return render(request, 'add_reservation.html', {'form': form})


def add_vehicle(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/')
    else:
        form = CarForm
    return render(request, 'add_car.html', {'form': form})


def vehicles(request):
    vehicles = Car.objects.filter(user=request.user)
    return render(request, 'vehicles.html', {"vehicles": vehicles})

