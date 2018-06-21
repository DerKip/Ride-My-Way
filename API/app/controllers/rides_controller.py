from models import rides
from models.rides import BaseRidesClass, all_ride_offers

from flask import request, jsonify
import json
from utils import JSON_MIME_TYPE, json_response

def create_new_ride_offer():
    """ Creates a new ride offer """
    data = request.json

    given_data = {
            "destination":data.get("destination"),
            "from_location":data.get("from_location"),
            "price":data.get("price"),
            "departure_time":data.get("departure_time")
    }

    if not all( 
                [ 
                  data.get("destination"),
                  data.get("from_location"),
                  data.get("price"),
                  data.get("departure_time")
                ]
            ):
        error = jsonify({'error': 'Missing field/s'})
        return json_response(error, 400)
   
    else:
        new_ride_offer = BaseRidesClass(
                            'Created_by: driver',
                            given_data["destination"],
                            given_data["from_location"],
                            given_data["price"],
                            given_data["departure_time"]
                            )
        rides.all_ride_offers.append(new_ride_offer.__dict__)
        return jsonify({"message": " Ride Offer Created Successfully"}),201
    



