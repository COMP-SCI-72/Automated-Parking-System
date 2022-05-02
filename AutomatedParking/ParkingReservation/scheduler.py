from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz
from django.utils import timezone
from .models import Reservation


def start_reservation(res):
    print("Starting reservation for ", res.user.username, " | ", res.start_date.strftime("%m/%d/%Y, %H:%M:%S %z"), " - ", res.end_date.strftime("%m/%d/%Y, %H:%M:%S %z"))
    if not res.parking_spot.occupied:
        res.parking_spot.occupied = True
    else:
        print("start_reservation attempted to start a reservation in an occupied spot | " + res.parking.name + ": "
              + res.parking_spot.row + ", " + res.parking_spot.col)
    res.parking_spot.save()


def end_reservation(res):
    res.parking_spot.occupied = False
    res.parking_spot.save()


def remove_overdue_reservations():
    print("remove_overdue_reservations called")
    reservation_table = Reservation.objects.all()
    for res in reservation_table:
        if res.end_date <= pytz.utc.localize(datetime.now()) and res.parking_spot.occupied:
            end_reservation(res)


def set_current_reservations():
    print("set_current_reservations called")
    reservation_table = Reservation.objects.all()
    for res in reservation_table:
        if res.start_date <= timezone.now() <= res.end_date and not res.parking_spot.occupied:
            start_reservation(res)


def start():
    scheduler = BackgroundScheduler()
    remove_overdue_reservations()
    set_current_reservations()
    scheduler.add_job(remove_overdue_reservations, 'interval', minutes=1)
    scheduler.add_job(set_current_reservations, 'interval', minutes=1)
    scheduler.start()
