from ...models.models import User ,get_users
from werkzeug.security import generate_password_hash
from flask import request, jsonify
import json
from utils import JSON_MIME_TYPE, json_response

def register_new_user():
    """ register a new driver """
    data = request.json

    given_data = {
            "username":data.get("username"),
            "email":data.get("email"),
            "car_model":data.get("car_model"),
            "car_regno":data.get("car_regno"),
            "contact":data.get("contact"),
            "password":data.get("password")
    }

    if not all( 
                [ 
                  data.get("username"),
                  data.get("email"),
                  data.get("car_model"),
                  data.get("car_regno"),
                  data.get("contact"),
                  data.get("password")
                ]
            ):
        error = jsonify({'error': 'Missing field/s'})
        return json_response(error, 400)

    new_user = User(
                    given_data["username"],
                    given_data["email"],
                    generate_password_hash(given_data["password"],method='sha256'),
                    given_data["car_model"],
                    given_data["car_regno"],
                    given_data["contact"]
                    )
    all_users = get_users()
    for user in all_users:
        if user["username"]== new_user.username:
            return jsonify({"message":"User already exists!"}),409
        elif user["email"]== new_user.email:
            return jsonify({"message":"Email already exists!"}),409
    new_user.create_user()
    return jsonify({"message":"Registration Successfull"}),201
