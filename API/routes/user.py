from flask import Blueprint, jsonify, request
from app.controllers import registration_controller, login_controller
from models.rides import all_ride_offers
from utils import JSON_MIME_TYPE, json_response
import datetime


user_route = Blueprint("route_user",__name__)
user_driver_route = Blueprint("route_user_driver",__name__)

@user_route.route('/register', methods=['POST'])
def register_user():
    """user registration endpoint"""
    if request.content_type != JSON_MIME_TYPE:
        error = jsonify({'error': 'Invalid Content Type'})
        return json_response(error, 400)
    return registration_controller.register_new_user()

@user_driver_route.route('/login', methods=['POST'])
def login_user():
    """login user endpoint"""
    if request.content_type != JSON_MIME_TYPE:
        error = jsonify({'error': 'Invalid Content Type'})
        return json_response(error, 400)
    return login_controller.login()



        # token = jwt.encode({'user':auth.username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},)
    error = jsonify({'error':'Could not verify!'})
    return json_response(error,401,{'WWW-Authenticate':'Basic realm="Login Required"'})
    
@user_route.route('/rides', methods=['GET'])
def get_all_ride_offers():
    """GET all ride offers endpoint"""
    rides = jsonify(all_ride_offers)
    return json_response(rides,200)

@user_route.route('/rides/<int:id>', methods=['GET'])
def get_single_ride_offer(id):
    """GET single ride offer endpoint"""
    single_ride_offer = [offer for offer in all_ride_offers if offer['id'] == id]
    return jsonify({"Your Ride Offer:":single_ride_offer}),200

