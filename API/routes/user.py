from flask import Blueprint, jsonify, request, Response
from app.controllers import registration_controller

from utils import JSON_MIME_TYPE, json_response

user_route = Blueprint("route_user",__name__)


@user_route.route('/register', methods=['POST'])
def register_user():
    """user registration endpoint"""

    if request.content_type != JSON_MIME_TYPE:
        error = jsonify({'error': 'Invalid Content Type'})
        return json_response(error, 400)
    return registration_controller.register_new_user()
    


    