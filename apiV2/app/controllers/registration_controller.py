from ...models.models import User ,get_users
from werkzeug.security import generate_password_hash
from flask import request, jsonify
from utils import JSON_MIME_TYPE, json_response
import re
import passwordmeter
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
    if given_data["username"] is not None and given_data["username"].strip() == "":
        return jsonify({'error': 'Required field/s Missing'}), 400
    if given_data["email"] is not None and given_data["email"].strip() == "":
        return jsonify({'error': 'Required field/s Missing'}), 400
    if given_data["contact"] is not None and given_data["contact"].strip() == "":
        return jsonify({'error': 'Required field/s Missing'}), 400
    if given_data["password"] is not None and given_data["password"].strip() == "":
        return jsonify({'error': 'Required field/s Missing'}), 400
    if given_data["confirm_password"] is not None and given_data["confirm_password"].strip() == "":
        return jsonify({'error': 'Required field/s Missing'}), 400        
    # check password strength using passwordmeter module
    if not re.match(r"[^@]+@[^@]+\.[^@]+", given_data["email"]):
        return jsonify({"error":"Your email is invalid"}),400
    meter = passwordmeter.Meter(settings=dict(factors='length,charmix'))
    strength, improvements = meter.test(given_data["password"])
    if strength < 0.2:
        
        return jsonify({"error":"""Your password is too weak, Consider this improvements <p> lenght: %(length)s<p> <p>charmix: %(charmix)s<p>""" %improvements}),400

    if given_data["password"] != given_data["confirm_password"]:
        return jsonify({"error":" Your passwords do no match"}),400
    new_user = User(
                    given_data["username"].lower(),
                    given_data["email"],
                    generate_password_hash(given_data["password"],method='sha256'),
                    given_data["car_model"],
                    given_data["car_regno"],
                    given_data["contact"]
                    )
    all_users = get_users()
    for user in all_users:
        if user["username"]== new_user.username:
            return jsonify({"error":"Username already taken!"}),409
        elif user["email"]== new_user.email:
            return jsonify({"error":"Email already exists!"}),409
    new_user.create_user()
    return jsonify({"message":"Registration Successfull"}),201
