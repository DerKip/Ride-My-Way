from flask import Blueprint, jsonify, request
from ..app.controllers import registration_controller, login_controller, rides_controller
from flask_jwt_extended import jwt_required,  get_jwt_identity  
from ..models.models import User,get_users, get_username, get_all_rides, get_ride_by_id, \
get_all_requests, insert_response, get_request_id
from utils import JSON_MIME_TYPE, json_response
import json

user_route = Blueprint("route_user",__name__)
auth = Blueprint("authenctiactaion",__name__)

@auth.route('/signup', methods=['POST'])
def register_user():
    """user registration endpoint"""
    if request.content_type != JSON_MIME_TYPE:
        error = jsonify({'error': 'Invalid Content Type'})
        return json_response(error, 400)
    return registration_controller.register_new_user()

@auth.route('/login', methods=['POST'])
def login_user():
    """login user endpoint"""
    if request.content_type != JSON_MIME_TYPE:
        error = jsonify({'error': 'Invalid Content Type'})
        return json_response(error, 400)
    return login_controller.login()

@user_route.route('/users', methods=['GET'])
def get_all_users():
    """GET all users endpoint"""
    users = get_users()
    return jsonify({"all users": users}),200
   
@user_route.route('/rides', methods=['POST'])
@jwt_required
def create_ride():
    user = get_jwt_identity() 
    user_id = get_username(user)
    """Create ride offer endpoint"""
    if request.content_type != JSON_MIME_TYPE:
        error = jsonify({'error': 'Invalid Content Type'})
        return json_response(error, 400)
    return rides_controller.create_new_ride_offer(user_id)

@user_route.route('/rides', methods=['GET'])
@jwt_required
def get_all_ride_offers():
    """GET all ride offers endpoint"""
    return jsonify({"all ride offers":get_all_rides()}),200

@user_route.route('/rides/<rideid>', methods=['GET'])
@jwt_required
def get_single_ride_offer(rideid):
    """GET single ride offer endpoint"""
    return jsonify({"Ride Offer:":get_ride_by_id(rideid)}),200

@user_route.route('/rides/<rideid>/request', methods=['POST'])
@jwt_required
def ride_request(rideid):
    """Make request to join ride endpoint"""
    ride_dict= dict(get_ride_by_id(rideid))
    rides_controller.make_ride_request(ride_dict["id"])
    return jsonify({"Message":"Successfully placed your request"},{"Ride Offer:":get_ride_by_id(rideid)}),200

@user_route.route('/rides/<rideid>/requests', methods=['GET'])
@jwt_required
def fetch_all_ride_requests(rideid):
    """Fetch all requests of a ride offer  endpoint"""
    all_ride_requests = get_all_requests(rideid)
    if len(all_ride_requests) == 0:
        return jsonify({"Message":"No requests sent to this ride offer"}),404
    return jsonify({"Your responses so far":all_ride_requests}),200

@user_route.route('/rides/<rideid>/requests/<requestid>', methods=['PUT','GET'])
@jwt_required
def accept_reject_response(rideid,requestid):
    """Accept or reject ride offer endpoint"""
    if get_ride_by_id(rideid) == None:
        return jsonify ({"message":"None-existent ride id"}),404
    status = request.json.get("Response")
    insert_response(status,requestid) 
    return jsonify({"Response_to_ride_offer":status},{"Request":get_request_id(requestid)}),200



