from flask import Blueprint, request, jsonify, make_response
from ..service.auth_service import AuthService

auth_controller = Blueprint("auth_controller", __name__)

@auth_controller.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = AuthService.register(data["username"], data["email"], data["password"])
    return jsonify({"id": user.id, "username": user.username, "email": user.email}), 201


@auth_controller.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    tokens = AuthService.login(data["email"], data["password"])

    response = make_response(jsonify(tokens))
    response.set_cookie("access_token", tokens["access_token"], httponly=True)
    response.set_cookie("refresh_token", tokens["refresh_token"], httponly=True)

    return response, 200

@auth_controller.route("/logout", methods=["POST"])
def logout():
    response = make_response(jsonify({"message": "Logged out"}))
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return response, 200

@auth_controller.route("/verify", methods=["GET"])
def verify():
    access_token = request.cookies.get("access_token")
    user = AuthService.verify(access_token)
    return jsonify(user), 200

@auth_controller.route("/refresh", methods=["POST"])
def refresh():
    refresh_token = request.cookies.get("refresh_token")
    tokens = AuthService.refresh(refresh_token)
    response = make_response(jsonify(tokens))
    response.set_cookie("access_token", tokens["access_token"], httponly=True)
    return response, 200


