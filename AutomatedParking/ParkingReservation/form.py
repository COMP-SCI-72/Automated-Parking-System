from django import forms
from django.forms import ModelForm
from .models import Reservation, Car


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('car', 'parking', 'start_date', 'end_date')


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'license')
