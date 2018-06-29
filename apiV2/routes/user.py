from flask import Blueprint, jsonify, request
from apiV2 import app
from ..app.controllers import registration_controller, login_controller, rides_controller
from flask_jwt_extended import jwt_required,  get_jwt_identity
from ..models.models import User,get_users, get_all_rides
from utils import JSON_MIME_TYPE, json_response
import datetime

user_route = Blueprint("route_user",__name__)
auth= Blueprint("authenctiactaion",__name__)

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
def create_ride():
    user_id = get_jwt_identity()
    """Create ride offer endpoint"""
    if request.content_type != JSON_MIME_TYPE:
        error = jsonify({'error': 'Invalid Content Type'})
        return json_response(error, 400)
    return rides_controller.create_new_ride_offer(user_id)


@user_route.route('/rides', methods=['GET'])
def get_all_ride_offers():
    """GET all ride offers endpoint"""
    return jsonify({"all ride offers":get_all_rides()}),200


# @user_route.route('/logout', methods=['DELETE'])
# def logout_user():
#     """user logout endpoint"""
#     return jsonify({"message":"Successfully logged out"}),200

# @user_route.route('/rides/<int:id>', methods=['GET'])
# def get_single_ride_offer(id):
#     """GET single ride offer endpoint"""
#     single_ride_offer = [offer for offer in all_ride_offers if offer['id'] == id]
#     if len(single_ride_offer) == 0:
#         abort(404)
#     return jsonify({"Ride Offer:":single_ride_offer}),200

# @user_route.route('/rides/<int:id>/join', methods=['POST'])
# def join_ride_offer(id):
#     """Join ride endpoint"""
#     single_ride_offer = [offer for offer in all_ride_offers if offer['id'] == id]
#     if len(single_ride_offer) == 0:
#         return jsonify({"message":"Not Found !"}),404
#     else:
#         single_ride_offer[0]["joined"] = "user"
#     return jsonify({"message":"Successfully joined ride"}),200

# @user_route.route('/rides/joined',methods=['GET'])
# def get_all_joined_ride_offer():
#     """Get all Joined rides endpoint"""
#     joined_rides = [ ride for ride in all_ride_offers if ride.get("joined",None) == "user"]
#     if len(joined_rides) == 0:
#         return jsonify({"message":"No joined Rides!"}),404
#     return jsonify({"All joined rides":joined_rides}),200