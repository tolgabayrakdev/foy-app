from flask import Flask, jsonify
from model import db
from exceptions import AppException

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


if __name__ == "__main__":
    app.run(debug=True)