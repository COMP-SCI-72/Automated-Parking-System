from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Parking(models.Model):
    name = models.CharField('Parking Name', max_length=150)
    parking_address = models.CharField(max_length=250)
    parking_zip = models.CharField('Zip Code', max_length=8)
    parking_city = models.CharField('City', max_length=50)
    parking_state = models.CharField('State', max_length=50)
    parking_spots = models.IntegerField()
    free_parking_spots = models.IntegerField()

    def __str__(self):
        return self.name


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField('Make', max_length=150)
    model = models.CharField('Model', max_length=150)
    year = models.IntegerField()
    license = models.CharField('License plate', max_length=150)

    def __str__(self):
        return "{} {} {}".format(self.make, self.model, self.year)


class Reservation(models.Model):
    # added separate start date and end date
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    # changed from date -> creation_date
    creation_date = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, blank=False, on_delete=models.CASCADE)
    price = models.IntegerField()
    parking = models.ForeignKey(Parking, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.user, self.creation_date, self.price)
