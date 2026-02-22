from dataclasses import dataclass


@dataclass
class Driver:
    id: str
    lat: float
    lon: float
    available: bool

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "lat": self.lat,
            "lon": self.lon,
            "available": self.available,
        }
