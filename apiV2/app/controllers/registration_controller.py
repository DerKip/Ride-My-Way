from ...models.models import User ,get_users
from werkzeug.security import generate_password_hash
from flask import request, jsonify
from utils import JSON_MIME_TYPE, json_response
from validate_email import validate_email
import passwordmeter
import sys
import json

def register_new_user():
    """ register a new driver """
    data = request.json

    given_data = {
            "username":data.get("username"),
            "email":data.get("email"),
            "car_model":data.get("car_model"),
            "car_regno":data.get("car_regno"),
            "contact":data.get("contact"),
            "password":data.get("password"),
            "confirm_password":data.get("confirm_password")
    }

    if not all( 
                [ 
                  data.get("username"),
                  data.get("email"),
                  data.get("contact"),
                  data.get("password")
                ]
            ):
        error = jsonify({'error': 'Required field/s Missing'})
        return json_response(error, 400)
    # check password strength using passwordmeter module
    meter = passwordmeter.Meter(settings=dict(factors='length,charmix'))
    strength, improvements = meter.test(given_data["password"])
    if strength < 0.2:
        return jsonify({"Your password is too week, Consider this improvements":improvements}),400

    if given_data["password"] != given_data["confirm_password"]:
        return jsonify({"message":" Your passwords do no match"}),400

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
