import math

from models.driver import Driver
from models.ride import Ride


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Great-circle distance in km between two lat/lon points."""
    R = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def match_rides_to_drivers(rides: list[Ride], drivers: list[Driver]) -> list[dict]:
    """
    Greedy priority-first matching: high-priority rides are assigned first,
    each to the nearest available driver. Drivers are not double-booked within
    a single match run. The source data is never mutated.
    """
    available = {d.id: d for d in drivers if d.available}
    sorted_rides = sorted(rides, key=lambda r: (r.priority_rank, r.id))

    results = []
    for ride in sorted_rides:
        if not available:
            results.append({
                "ride_id": ride.id,
                "driver_id": None,
                "distance_km": None,
                "priority": ride.priority,
            })
            continue

        best_driver = min(
            available.values(),
            key=lambda d: haversine_km(d.lat, d.lon, ride.start_lat, ride.start_lon),
        )
        dist = haversine_km(best_driver.lat, best_driver.lon, ride.start_lat, ride.start_lon)

        results.append({
            "ride_id": ride.id,
            "driver_id": best_driver.id,
            "distance_km": round(dist, 3),
            "priority": ride.priority,
        })
        del available[best_driver.id]

    return results
