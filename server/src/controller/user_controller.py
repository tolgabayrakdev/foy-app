from flask import Blueprint, request, jsonify
from ..service.user_service import UserService

user_controller = Blueprint("user_controller", __name__)

@user_controller.route("/update-user", methods=["PUT"])
def update_user():
    data = request.get_json()
    user = UserService.update_user(data["id"], username=data["username"], email=data["email"])
    return jsonify({"id": user.id, "username": user.username, "email": user.email}), 200

