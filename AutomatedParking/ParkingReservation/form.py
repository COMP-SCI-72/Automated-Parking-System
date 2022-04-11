from django import forms
from django.forms import ModelForm
from .models import Reservation, Car
from django.contrib.auth.models import User


class ReservationForm(ModelForm):

    class Meta:
        model = Reservation
        fields = ('car', 'parking', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(ReservationForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['car'].queryset = Car.objects.filter(user=self.user)


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'license')
