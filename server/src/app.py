from flask import Flask, jsonify
from flask_cors import CORS
from .model import db
from .exceptions import AppException

# controllers
from .controller.auth_controller import auth_controller
from .controller.user_controller import user_controller
from .controller.student_controller import student_controller

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5432/postgres"

@app.errorhandler(AppException)
def handle_app_exception(error):
    response = jsonify({"error": error.message})
    response.status_code = error.status_code
    return response

db.init_app(app)
with app.app_context():
    db.create_all()

CORS(app, supports_credentials=True)

app.register_blueprint(auth_controller, url_prefix="/api/auth")
app.register_blueprint(user_controller, url_prefix="/api")
app.register_blueprint(student_controller, url_prefix="/api/students")

if __name__ == "__main__":
    app.run(debug=True)