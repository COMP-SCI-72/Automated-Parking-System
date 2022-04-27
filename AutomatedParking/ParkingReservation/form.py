from datetime import datetime
from django import forms
from django.forms import ModelForm
from .models import Reservation, Car, ParkingSpot, Parking
from django.contrib.auth.models import User


class ReservationForm(ModelForm):

    start_time = forms.TimeField()
    end_time = forms.TimeField()

    CUSTOM_TIME_FORMAT = '%I:%M %p'

    class Meta:
        model = Reservation
        fields = ('car', 'parking', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(ReservationForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['car'].queryset = Car.objects.filter(user=self.user)
        # allow AM/PM time format
        if self.CUSTOM_TIME_FORMAT not in self.fields['start_time'].input_formats:
            self.fields['start_time'].input_formats.append(self.CUSTOM_TIME_FORMAT)
        if self.CUSTOM_TIME_FORMAT not in self.fields['end_time'].input_formats:
            self.fields['end_time'].input_formats.append(self.CUSTOM_TIME_FORMAT)


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'license')
