import jwt
from datetime import datetime, timedelta
from ..exceptions import AppException

SECRET_KEY = "your-very-secret-key"
ACCESS_TOKEN_EXPIRE_MINUTES = 1
REFRESH_TOKEN_EXPIRE_DAYS = 7

def create_access_token(user_id):
    expiration = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "user_id": user_id,
        "exp": expiration,
        "type": "access"
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def create_refresh_token(user_id):
    expiration = datetime.now() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    payload = {
        "user_id": user_id,
        "exp": expiration,
        "type": "refresh"
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise AppException("Token has expired", 401)
    except jwt.InvalidTokenError:
        raise AppException("Invalid token", 401)
