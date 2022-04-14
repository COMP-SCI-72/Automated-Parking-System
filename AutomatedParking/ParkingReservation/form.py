from django import forms
from django.forms import ModelForm
from .models import Reservation, Car, ParkingSpot, Parking
from django.contrib.auth.models import User


class ReservationForm(ModelForm):

    class Meta:
        model = Reservation
        fields = ('car', 'parking', 'start_date', 'end_date', 'parking_spot')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(ReservationForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['car'].queryset = Car.objects.filter(user=self.user)
            self.fields['parking_spot'].queryset = ParkingSpot.objects.none()

        if 'parking' in self.data:
            try:
                parking_id = int(self.data.get('parking'))
                self.fields['parking_spot'].queryset = ParkingSpot.objects.filter(parking_id=parking_id).order_by('row')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['parking_spot'].queryset = self.instance.parking.parking_spot_set.order_by('row')


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'license')
