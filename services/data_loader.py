import csv
import os

from models.driver import Driver
from models.ride import Ride

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_rides(path: str = None) -> list[Ride]:
    path = path or os.path.join(_ROOT, "data", "ride_requests.csv")
    rides = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            rides.append(Ride(
                id=int(row["id"]),
                start_lat=float(row["start_lat"]),
                start_lon=float(row["start_lon"]),
                end_lat=float(row["end_lat"]),
                end_lon=float(row["end_lon"]),
                priority=row["priority"].strip().lower(),
            ))
    return rides


def load_drivers(path: str = None) -> list[Driver]:
    path = path or os.path.join(_ROOT, "data", "drivers.csv")
    drivers = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            drivers.append(Driver(
                id=row["id"].strip(),
                lat=float(row["lat"]),
                lon=float(row["lon"]),
                available=row["available"].strip().lower() == "true",
            ))
    return drivers
