from ...models.models import  Rides, Requests ,get_all_requests
from flask import request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import json
from utils import JSON_MIME_TYPE, json_response

def create_new_ride_offer(created_by):
    """ Creates a new ride offer """
    data = request.json
    given_data = {
            "created_by":created_by,
            "destination":data.get("destination"),
            "from_location":data.get("from_location"),
            "price":data.get("price"),
            "departure_time":data.get("departure_time")
    }

    if not all( 
                [ 
                  data.get("destination"),
                  data.get("from_location"),
                  data.get("departure_time")
                ]
            ):
        error = jsonify({'error': 'Missing field/s'})
        return json_response(error, 400)
   
    else:
        new_ride_offer = Rides(
                                given_data["created_by"],
                                given_data["destination"],
                                given_data["from_location"],
                                given_data["price"],
                                given_data["departure_time"]
                            )
        new_ride_offer.create_ride()
        return jsonify({"Created_ride_offer":new_ride_offer.__dict__}),201

def make_ride_request(ride_id):
    """Makes a request to join a ride offer"""
    user_id = get_jwt_identity()
    response ='Interested'
    new_request = Requests(user_id,ride_id,response)
    return  new_request.create_request()


