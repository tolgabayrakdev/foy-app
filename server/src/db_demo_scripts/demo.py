from src.model import User

email = "deneme123@gmail.com"

user = User.query.filter_by(email=email).first()
