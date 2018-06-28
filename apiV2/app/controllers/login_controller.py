from ...models import driver, user
from ...models.user import users
from ...models.driver import drivers
from werkzeug.security import check_password_hash
from flask import request, jsonify
import json
from utils import JSON_MIME_TYPE, json_response 


def login():
    """ Controlls user log in """
    if not request.json.get('username'):
        error = jsonify({"error":"username is required!"})
        return json_response(error,400)

    if not request.json.get('password'):
        error = jsonify({"error":"Password is required!"})
        return json_response(error,400)

    given_data = {
                  "username":request.json.get("username"),
                  "password":request.json.get("password"),
                  }   
    #Check if username exists in the in the driver model                  
    if any(d.get('username', None) == given_data["username"] for d in driver.drivers):
        #place the driver data in a dict
        driver_data = [ x for x in driver.drivers if x["username"]== given_data["username"]][0]

        if check_password_hash(driver_data["password"],given_data["password"]) == True:
            return jsonify({
                            "message": "Login successfull!",
                            "status": "Driver"
                            }),200
        return jsonify({
                        "error": "password incorrect!",
                        }),400

    #Check if username exists in the in the user model                  
    if any(d.get('username', None) == given_data["username"] for d in user.users):
        #place the driver data in a dict
        user_data = [ x for x in user.users if x["username"]== given_data["username"]][0]

        if check_password_hash(user_data["password"],given_data["password"]) == True:
            return jsonify({
                            "message": "Login successfull!",
                            "status": "Passenger"
                            }),200
        return jsonify({
                        "error": "Password incorrect!",
                        }),400
    return jsonify({
                        "error": "User does not exist!",
                        }),400       