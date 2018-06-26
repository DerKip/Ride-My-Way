from flask import Blueprint, jsonify, request, Response

from ..app.controllers import registration_controller, rides_controller
from ..models.rides import all_ride_offers

from utils import JSON_MIME_TYPE, json_response

driver_route = Blueprint("route_driver",__name__)


@driver_route.route('/register', methods=['POST'])
def register_driver():
    """Driver registration endpoint"""

    if request.content_type != JSON_MIME_TYPE:
        error = jsonify({'error': 'Invalid Content Type'})
        return json_response(error, 400)
    return registration_controller.register_new_driver()

@driver_route.route('/logout', methods=['DELETE'])
def logout_driver():
    """Driver logout endpoint"""
    return jsonify({"message":"Successfully logged out"}),200
    
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

@driver_route.route('/rides/<int:id>', methods=['GET'])
def get_single_ride_offer(id):
    """GET single ride offer endpoint"""
    single_ride_offer = [offer for offer in all_ride_offers if offer['id'] == id]
    return jsonify({"Your Ride Offer:":single_ride_offer}),200

@driver_route.route('/rides/<string:driver>', methods=['GET'])
def get_all_my_ride_offers(driver):
    """GET all my ride offers endpoint"""
    my_rides =[rides for rides in all_ride_offers if rides["created_by"] == driver]
    return jsonify({(("{} ride offers").format(driver)):my_rides})