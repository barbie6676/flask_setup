from flask import Blueprint, jsonify

from services.data_loader import load_rides

rides_bp = Blueprint("rides", __name__)


@rides_bp.get("/rides")
def get_rides():
    return jsonify([r.to_dict() for r in load_rides()])
