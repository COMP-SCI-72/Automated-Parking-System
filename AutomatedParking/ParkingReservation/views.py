from datetime import datetime

from django.shortcuts import render, redirect
from .models import Reservation, Car, Parking, ParkingSpot
from .form import ReservationForm, CarForm
from .assigner import find_open_spot
from django.http import HttpResponseRedirect
from django.contrib import messages
import pytz


def home(request):
    return render(request, 'index.html', {})


def user_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations.html', {"reservations": reservations})


def add_reservations(request):
    if request.method == "POST":
        form = ReservationForm(request.POST, user=request.user)
        if form.is_valid():
            obj = form.save(commit=False)

            local_tz = pytz.timezone("America/Chicago")
            start = datetime.combine(form.cleaned_data['start_date'], form.cleaned_data['start_time'])
            end = obj.end_date = datetime.combine(form.cleaned_data['end_date'], form.cleaned_data['end_time'])
            obj.start_date = local_tz.localize(start).astimezone(pytz.utc)
            obj.end_date = local_tz.localize(end).astimezone(pytz.utc)

            spot = find_open_spot(obj)
            if spot:
                obj.parking_spot = spot
                obj.price = obj.parking_spot.cost_per_hour
                obj.user = request.user
                obj.save()

                return HttpResponseRedirect('/reservations')
            else:
                messages.success(request, "There is no spot available in " + obj.parking.name + " for that time period.")

    else:
        form = ReservationForm(user=request.user)
    return render(request, 'add_reservation.html', {'form': form})


def remove_reservation(request, reservation_id):
    res = Reservation.objects.get(id=reservation_id)
    spot = ParkingSpot.objects.get(id=res.parking_spot.id)
    spot.occupied = False
    spot.save()
    res.delete()
    return HttpResponseRedirect('/reservations')


def add_vehicle(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/vehicles')
    else:
        form = CarForm
    return render(request, 'add_car.html', {'form': form})


def remove_vehicle(request, vehicle_id):
    vehicle = Car.objects.get(id=vehicle_id)
    vehicle.delete()
    print("remove_vehicle " + str(vehicle_id))
    return HttpResponseRedirect('/vehicles')


def vehicles(request):
    v = Car.objects.filter(user=request.user)
    return render(request, 'vehicles.html', {"vehicles": v})


def load_parking_spots(request):
    parking_id = request.GET.get('parking_id')
    parking_spots = ParkingSpot.objects.filter(parking_id=parking_id, occupied=False)
    return render(request, 'parking_spots_dropdown.html', {"parking_spots": parking_spots})
