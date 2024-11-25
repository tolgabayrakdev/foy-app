from ..model import db, Milestone
from ..exceptions import AppException


class MilestoneService:

    @staticmethod
    def create_milestone(data):
        try:
            milestone = Milestone(**data)
            db.session.add(milestone)
            db.session.commit()
            return milestone
        except Exception as e:
            db.session.rollback()
            raise AppException(str(e), 500)

    @staticmethod
    def update_milestone(data, id):
        try:
            db.session.begin()
            milestone = Milestone.query.filter_by(id=id).first()
            if not milestone:
                raise AppException("Milestone not found", 404)

            for key, value in data.items():
                setattr(milestone, key, value)

            db.session.commit()
            return milestone
        except Exception as e:
            db.session.rollback()
            raise AppException(str(e), 500)

    @staticmethod
    def delete_milestone(id):
        milestone = Milestone.query.filter_by(id=id).first()
        if not milestone:
            raise AppException("Milestone not found", 404)
        db.session.delete(milestone)
        db.session.commit()
        return True


    @staticmethod
    def get_milestone(id):
        milestone = Milestone.query.filter_by(id=id).first()
        if not milestone:
            raise AppException("Milestone not found", 404)
        return milestone

    @staticmethod
    def list_milestones(goal_id):
        milestones = Milestone.query.filter_by(goal_id=goal_id).all()
        return milestones