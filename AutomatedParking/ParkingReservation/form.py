from django import forms
from django.forms import ModelForm
from .models import Reservation, Car


class ReservationForm(ModelForm):

    class Meta:
        model = Reservation
        fields = ('car', 'parking')  #'__all__'


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'license')

