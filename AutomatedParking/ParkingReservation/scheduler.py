from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz
from .models import Reservation


def start_reservation(res):
    res.parking_spot.occupied = True
    res.parking_spot.save()


def end_reservation(res):
    res.parking_spot.occupied = False
    res.parking_spot.save()


def remove_overdue_reservations():
    # debugging
    print("remove_overdue_reservations called")
    reservation_table = Reservation.objects.all()
    for res in reservation_table:
        if res.end_date <= pytz.utc.localize(datetime.now()) and res.parking_spot.occupied:
            end_reservation(res)


def set_current_reservations():
    # debugging
    print("set_current_reservations called")
    reservation_table = Reservation.objects.all()
    for res in reservation_table:
        if res.start_date <= pytz.utc.localize(datetime.now()) <= res.end_date and not res.parking_spot.occupied:
            start_reservation(res)


def start():
    scheduler = BackgroundScheduler()
    remove_overdue_reservations()
    set_current_reservations()
    scheduler.add_job(remove_overdue_reservations, 'interval', minutes=1)
    scheduler.add_job(set_current_reservations, 'interval', minutes=1)
    scheduler.start()
