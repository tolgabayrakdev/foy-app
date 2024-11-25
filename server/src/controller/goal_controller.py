from flask import Blueprint, request, jsonify
from ..service.goal_service import GoalService
from ..decorator.token_required import token_required

goal_controller = Blueprint("goal_controller", __name__)


@goal_controller.route("/", methods=["POST"])
@token_required
def create_goal():
    data = request.get_json()
    goal = GoalService.create_goal(data, request.user["user_id"])
    return jsonify(goal.to_dict()), 201

@goal_controller.route("/", methods=["GET"])
@token_required
def list_goals():
    goals = GoalService.list_goals(request.user["user_id"])
    return jsonify(goals), 200

@goal_controller.route("/<int:id>", methods=["GET"])
@token_required
def get_goal(id):
    goal = GoalService.get_goal(id)
    return jsonify(goal), 200

@goal_controller.route("/<int:id>", methods=["PUT"])
@token_required
def update_goal(id):
    data = request.get_json()
    goal = GoalService.update_goal(data, id)
    return jsonify(goal), 200

@goal_controller.route("/<int:id>", methods=["DELETE"])
@token_required
def delete_goal(id):
    GoalService.delete_goal(id)
    return jsonify({"message": "Goal deleted"}), 200