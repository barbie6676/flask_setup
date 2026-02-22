from flask import Blueprint, jsonify

from services.data_loader import load_drivers

drivers_bp = Blueprint("drivers", __name__)


@drivers_bp.get("/drivers")
def get_drivers():
    return jsonify([d.to_dict() for d in load_drivers()])
