from ..model import db, Goal
from ..exceptions import AppException


class GoalService:
    @staticmethod
    def create_goal(data, user_id):
        try:
            db.session.begin()
            goal = Goal(**data, user_id=user_id)
            db.session.add(goal)
            db.session.commit()
            return goal
        except Exception as e:
            db.session.rollback()
            raise AppException(str(e), 500)

    @staticmethod
    def get_goal(id):
        goal = Goal.query.filter_by(id=id).first()
        if not goal:
            raise AppException("Goal not found", 404)
        return goal

    @staticmethod
    def list_goals(user_id):
        query = Goal.query
        if user_id:
            query = query.filter_by(user_id=user_id)
        return query.all()

    @staticmethod
    def update_goal(data, id):
        try:
            db.session.begin()
            goal = Goal.query.filter_by(id=id).first()
            if not goal:
                raise AppException("Goal not found", 404)

            for key, value in data.items():
                setattr(goal, key, value)

            db.session.commit()
            return goal
        except Exception as e:
            db.session.rollback()
            raise AppException(str(e), 500)

    @staticmethod
    def delete_goal(id):
        goal = Goal.query.filter_by(id=id).first()
        if not goal:
            raise AppException("Goal not found", 404)
        db.session.delete(goal)
        db.session.commit()
        return True

    @staticmethod
    def update_completion_percentage(goal_id, completion_percentage):
        try:
            db.session.begin()

            goal = Goal.query.filter_by(id=goal_id).first()
            if not goal:
                raise AppException("Goal not found", 404)

            if not (0 <= completion_percentage <= 100):
                raise AppException("Completion percentage must be between 0 and 100", 400)

            goal.completion_percentage = completion_percentage
            db.session.commit()
            return goal
        except Exception as e:
            db.session.rollback()
            raise AppException(str(e), 500)