from marshmallow import ValidationError

from ..model import db, User
from ..exceptions import AppException
from werkzeug.security import generate_password_hash, check_password_hash
from ..helper.jwt_helper import create_access_token, create_refresh_token, decode_token
from ..schema.auth_schema import UserRegistrationSchema, LoginSchema
import jwt

schema = UserRegistrationSchema()
login_schema = LoginSchema()

class AuthService:
    @staticmethod
    def register(username: str, email: str, password: str):
        try:
            validated_data = schema.load({"username": username, "email": email, "password": password})
            username = validated_data['username']
            email = validated_data['email']
            password = validated_data['password']

            if User.query.filter_by(username=username).first():
                raise AppException("User already exists", 400)

            if User.query.filter_by(email=email).first():
                raise AppException("Email already exists", 400)

            hashed_password = generate_password_hash(password)
            user = User(username=username, email=email, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return user
        except ValidationError as e:
            raise AppException(e.messages, 400)

    @staticmethod
    def login(email: str, password: str):
        try:
            validated_data = login_schema.load({"email": email, "password": password})
            email = validated_data['email']
            password = validated_data['password']

            user = User.query.filter_by(email=email).first()
            if not user or not check_password_hash(user.password, password):
                raise AppException("Invalid email or password", 401)

            access_token = create_access_token(user.id)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}
        except ValidationError as e:
            raise AppException(e.messages, 400)

    @staticmethod
    def verify(token):
        if not token:
            raise AppException("Unauthorized", 401)
        try:
            payload = decode_token(token)
            user_id = payload["user_id"]
            user = User.query.filter_by(id=user_id).first()
            if not user:
                raise AppException("Unauthorized", 401)
            return {"id": user.id, "username": user.username, "email": user.email}
        except AppException as e:
            raise AppException(e.message, e.status_code)
        except Exception as e:
            raise AppException(str(e), 500)

    @staticmethod
    def refresh(refresh_token):
        if not refresh_token:
            raise AppException("Unauthorized", 401)
        try:
            payload = decode_token(refresh_token)
            if payload["type"] != "refresh":
                raise AppException("Invalid token", 401)
            user_id = payload["user_id"]
            access_token = create_access_token(user_id)
            return {"access_token": access_token}
        except jwt.ExpiredSignatureError:
            raise AppException("Token has expired, Please login again", 401)
        except jwt.InvalidTokenError:
            raise AppException("Invalid token", 401)
        except Exception as e:
            raise AppException(str(e), 500)

