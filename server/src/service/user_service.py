from ..model import db, User
from ..exceptions import AppException

class UserService:

    @staticmethod
    def update_user(user_id, **kwargs):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            raise AppException("User not found", 404)
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()
        return user
    
    @staticmethod
    def change_password(user_id, new_password):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            raise AppException("User not found", 404)
        user.password = new_password
        db.session.commit()
        return user