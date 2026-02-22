from dataclasses import dataclass
from typing import Literal

PRIORITY_RANK = {"high": 1, "medium": 2, "low": 3}


@dataclass
class Ride:
    id: int
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float
    priority: Literal["high", "medium", "low"]

    @property
    def priority_rank(self) -> int:
        return PRIORITY_RANK.get(self.priority, 99)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "start_lat": self.start_lat,
            "start_lon": self.start_lon,
            "end_lat": self.end_lat,
            "end_lon": self.end_lon,
            "priority": self.priority,
        }
