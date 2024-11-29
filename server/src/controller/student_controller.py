from flask import Blueprint, request, jsonify
from ..service.student_service import StudentService
from ..decorator.token_required import token_required
from ..exceptions import AppException

student_controller = Blueprint("student_controller", __name__)


@student_controller.route("/", methods=["GET"])
@token_required
def get_all_students():
    user_id = request.user["user_id"]
    students = StudentService.get_all_students(user_id)
    return jsonify([student.to_dict() for student in students]), 200


@student_controller.route("/<int:student_id>", methods=["GET"])
@token_required
def get_student_by_id(student_id):
    student = StudentService.get_student_by_id(student_id)
    return jsonify(student.to_dict()), 200


@student_controller.route("/", methods=["POST"])
@token_required
def create_student():
    data = request.get_json()
    new_student = StudentService.create_student(data)
    return jsonify(new_student.to_dict()), 201


@student_controller.route("/<int:student_id>", methods=["PUT"])
@token_required
def update_student(student_id):
    data = request.get_json()
    updated_student = StudentService.update_student(student_id, data)
    return jsonify(updated_student.to_dict()), 200


@student_controller.route("/<int:student_id>", methods=["DELETE"])
@token_required
def delete_student(student_id):
    StudentService.delete_student(student_id)
    return jsonify({"message": "Student deleted successfully"}), 200
