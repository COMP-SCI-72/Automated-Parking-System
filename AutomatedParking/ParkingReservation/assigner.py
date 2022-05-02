import pytz

from .models import Reservation, Parking, ParkingSpot


def find_open_spot(res):
    garage = res.parking
    start = res.start_date
    end = res.end_date

    # get all reservations for the selected garage
    reservations = Reservation.objects.filter(parking=garage)

    # get all parking spots for the garage
    spots = list(ParkingSpot.objects.filter(parking=garage))

    for r in reservations:
        if start <= r.start_date <= end or start <= r.end_date <= end:
            spots.remove(r.parking_spot)

    if spots:
        return spots[0]
    else:
        return None
