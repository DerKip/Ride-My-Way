from flask import Blueprint, jsonify, request, Response

from app.controllers import registration_controller, rides_controller
from models.rides import all_ride_offers

from utils import JSON_MIME_TYPE, json_response

driver_route = Blueprint("route_driver",__name__)


@driver_route.route('/register', methods=['POST'])
def register_driver():
    """Driver registration endpoint"""

    if request.content_type != JSON_MIME_TYPE:
        error = jsonify({'error': 'Invalid Content Type'})
        return json_response(error, 400)
    return registration_controller.register_new_driver()
    


@driver_route.route('/create_ride', methods=['POST'])
def create_ride():
    """Create ride offer endpoint"""

    if request.content_type != JSON_MIME_TYPE:
        error = jsonify({'error': 'Invalid Content Type'})
        return json_response(error, 400)

    return rides_controller.create_new_ride_offer()



@driver_route.route('/rides', methods=['GET'])
def get_all_ride_offers():
    """GET all ride offers endpoint"""
    rides = jsonify(all_ride_offers)
    return json_response(rides,200)