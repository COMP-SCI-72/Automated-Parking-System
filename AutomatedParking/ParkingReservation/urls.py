from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('reservations', views.user_reservations, name="reservations"),
    path('vehicles', views.vehicles, name="vehicles"),
    path('add-reservations', views.add_reservations, name="add-reservations"),
    path('add-vehicle', views.add_vehicle, name="add-vehicle"),
]