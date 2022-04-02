from django import forms
from django.forms import ModelForm
from .models import Reservation, Car


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

