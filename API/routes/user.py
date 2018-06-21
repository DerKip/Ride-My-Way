from flask import Blueprint, jsonify, request, Response
from app.controllers import registration_controller
from models.rides import all_ride_offers
from utils import JSON_MIME_TYPE, json_response

user_route = Blueprint("route_user",__name__)


@user_route.route('/register', methods=['POST'])
def register_user():
    """user registration endpoint"""

    if request.content_type != JSON_MIME_TYPE:
        error = jsonify({'error': 'Invalid Content Type'})
        return json_response(error, 400)
    return registration_controller.register_new_user()


@user_route.route('/rides', methods=['GET'])
def get_all_ride_offers():
    """GET all ride offers endpoint"""
    rides = jsonify(all_ride_offers)
    return json_response(rides,200)
    


    