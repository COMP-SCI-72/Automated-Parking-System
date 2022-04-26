from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('reservations', views.user_reservations, name="reservations"),
    path('vehicles', views.vehicles, name="vehicles"),
    path('add-reservations', views.add_reservations, name="add-reservations"),
    path('reservations/remove-reservation/<int:reservation_id>', views.remove_reservation, name="remove-reservation"),
    path('ajax/load-parking-spots', views.load_parking_spots, name="ajax_load_parking_spots"),
    path('add-vehicle', views.add_vehicle, name="add-vehicle"),
    path('vehicles/remove-vehicle/<int:vehicle_id>', views.remove_vehicle, name="remove-vehicle"),
]