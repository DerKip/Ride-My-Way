from ...models import driver, user
from ...models.user import UserData ,users
from ...models.driver import DriverData ,drivers
from werkzeug.security import generate_password_hash
from flask import request, jsonify
import json
from utils import JSON_MIME_TYPE, json_response

def register_new_driver():
    """ register a new driver """
    data = request.json

    given_data = {
            "username":data.get("username"),
            "email":data.get("email"),
            "car_model":data.get("car_model"),
            "car_regno":data.get("car_regno"),
            "password":data.get("password")
    }

    if not all( 
                [ 
                  data.get("username"),
                  data.get("email"),
                  data.get("car_model"),
                  data.get("car_regno"),
                  data.get("password")
                ]
            ):
        error = jsonify({'error': 'Missing field/s'})
        return json_response(error, 400)
    
    
    if not any(d.get('username', None) == given_data["username"] for d in driver.drivers):
        # checks if user name exists in the driver model and creates new object if not
        new_driver = DriverData(
                            given_data["username"],
                            given_data["email"],
                            generate_password_hash(given_data["password"],method='sha256'),
                            given_data["car_model"],
                            given_data["car_regno"]
                            )
        driver.drivers.append(new_driver.__dict__)
        return jsonify({"message": " Registration Successfull"}),201
    else:
        error = jsonify({"message":"User already exists!"})
        return json_response(error,409)




def register_new_user():
    """ register a new driver """
    data = request.json

    given_data = {
            "username":data.get("username"),
            "email":data.get("email"),
            "password":data.get("password")
    }

    if not all( 
                [ 
                  data.get("username"),
                  data.get("email"),
                  data.get("password")
                ]
            ):
        error = jsonify({'error': 'Missing field/s'})
        return json_response(error, 400)
    
    
    if not any(d.get('username', None) == given_data["username"] for d in user.users):
        # checks if user name exists in the driver model and creates new object if not
        new_user = UserData(
                            given_data["username"],
                            given_data["email"],
                            generate_password_hash(given_data["password"],method='sha256'),
                            )
        user.users.append(new_user.__dict__)
        return jsonify({"message": " Registration Successfull"}),201
    else:
        error = jsonify({"message":"User already exists!"})
        return json_response(error,409)
 
    
       
    

    
     

