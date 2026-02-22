from flask import Blueprint, jsonify

from services.data_loader import load_drivers, load_rides
from services.matcher import match_rides_to_drivers

match_bp = Blueprint("match", __name__)


@match_bp.get("/match")
def get_match():
    rides = load_rides()
    drivers = load_drivers()
    return jsonify(match_rides_to_drivers(rides, drivers))
