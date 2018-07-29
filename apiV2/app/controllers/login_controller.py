from ...models.models import User ,get_user
from werkzeug.security import check_password_hash
from flask import request, jsonify
from flask_jwt_extended import  jwt_required, create_access_token, get_jwt_identity
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
                  "username":request.json.get("username").lower(),
                  "password":request.json.get("password"),
                  }   
    #Check if username is in the  db
    login_visitor = get_user(given_data["username"])
    if login_visitor == None:
        return jsonify({"error": "User does not exist!"}),400
    elif check_password_hash(login_visitor["password"],given_data["password"]) == True:
        # Give access token 
        access_token = create_access_token(identity = login_visitor["id"])
        return jsonify({"message": "Login successfull!","token":access_token}),200
    return jsonify({"error": "password incorrect!"}),401

