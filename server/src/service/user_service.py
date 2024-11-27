from ..model import db, User
from ..exceptions import AppException
from werkzeug.security import generate_password_hash, check_password_hash

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
    def change_password(user_id, data):
        if "current_password" not in data or "new_password" not in data:
            raise AppException("Current password and new password are required", 400)
        
        user = User.query.filter_by(id=user_id).first()
        if not user:
            raise AppException("User not found", 404)
        
        if not check_password_hash(user.password, data["current_password"]):
            raise AppException("Current password is incorrect", 400)
        
        hashed_password = generate_password_hash(data["new_password"])
        user.password = hashed_password
        db.session.commit()
        return user