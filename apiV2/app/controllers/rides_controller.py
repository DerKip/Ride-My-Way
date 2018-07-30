from ...models.models import  Rides, Requests ,get_all_requests, get_ride_by_id, get_ride_user_time, \
get_username, get_driver_rides, update_ride_offer
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

    if given_data["destination"] is not None and given_data["destination"].strip() == "":
        return jsonify({'error': 'Required field/s Missing'}), 400
    if given_data["from_location"] is not None and given_data["from_location"].strip() == "":
        return jsonify({'error': 'Required field/s Missing'}), 400
    if given_data["departure_time"] is not None and given_data["departure_time"].strip() == "":
        return jsonify({'error': 'Required field/s Missing'}), 400
    
    else:
        new_ride_offer = Rides(
                                given_data["created_by"],
                                given_data["destination"],
                                given_data["from_location"],
                                given_data["price"],
                                given_data["departure_time"]
         
                           )  
        # check if there is an existing ride the user created with the same departure time
        user_id = get_jwt_identity()
        user = get_username(user_id)
        rides = get_ride_user_time(user,request.json.get("departure_time"))
        if len(rides) != 0:
            return jsonify({"error":"You already placed a ride offer at this time"}),400
        new_ride_offer.create_ride()
        return jsonify({"ride":new_ride_offer.__dict__ ,"message":"Successfully created ride offer"}),201

def make_ride_request(ride_id):
    """Makes a request to join a ride offer"""
    user_id = get_jwt_identity()
    response ='Interested'
    new_request = Requests(user_id,ride_id,response)
    return  new_request.create_request()

def update_ride(rideid):
    """ updates details of a ride offer """
    ride = get_ride_by_id(rideid)
    data = request.json
    given_data = {
            "destination":data.get("destination"),
            "from_location":data.get("from_location"), 
            "price":data.get("price"),
            "departure_time":data.get("departure_time")
            }
    if given_data["destination"]is not None and given_data["destination"].strip() == "":
        return jsonify({'error': 'input correct destination'}), 400
    if given_data["from_location"]is not None and given_data["from_location"].strip() == "":
        return jsonify({'error': 'input correct location'}), 400
    if given_data["departure_time"]is not None and given_data["departure_time"].strip() == "":
        return jsonify({'error': 'input correct departure_time'}), 400
    if given_data["price"]is not None and given_data["price"].strip() == "":
        return jsonify({'error': 'input correct price'}), 400

    destination = given_data["destination"]
    from_location = given_data["from_location"]
    price = given_data ["price"]
    departure_time = given_data ["departure_time"]

    if not all(given_data):
        return jsonify({"message":"No changes made "},{"ride offer":get_ride_by_id(rideid)}),200
    # revert back to original details if none is given
    if destination == None :
        destination = ride["destination"]
    if from_location == None :
        from_location = ride["from_location"]
    if departure_time == None:
        departure_time = ride["departure_time"]
    if price == None :
        price = ride["price"]
    
    # update ride offer in rides model
    update_ride_offer(rideid,destination,from_location,price,departure_time)
    return jsonify({"message":"Successfully Updated ride offer"},{"updated ride offer":get_ride_by_id(rideid)}),200
    

