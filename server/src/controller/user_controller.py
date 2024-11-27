from flask import Blueprint, request, jsonify
from ..service.user_service import UserService
from ..decorator.token_required import token_required
from ..exceptions import AppException

user_controller = Blueprint("user_controller", __name__)

@user_controller.route("/update-user", methods=["PUT"])
@token_required
def update_user():
    data = request.get_json()
    user = UserService.update_user(request.user["user_id"], **data)
    return jsonify({"id": user.id, "username": user.username, "email": user.email}), 200


@user_controller.route("/change-password", methods=["POST"])
@token_required
def change_password():
    data = request.get_json()
    user = UserService.change_password(request.user["user_id"], data)
    return jsonify({"id": user.id, "username": user.username, "email": user.email}), 200