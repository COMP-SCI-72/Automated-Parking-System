from django.apps import AppConfig
from os import environ


class ParkingreservationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ParkingReservation'

    def ready(self):
        if environ.get('RUN_MAIN', None) != 'true':
            # debugging
            print("ParkingReservation ready function called")
            from . import scheduler
            scheduler.start()
