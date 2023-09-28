from flask import Blueprint, jsonify
from main import db
from models.users import User
from schemas.users import user_schema, users_schema

users = Blueprint("users", __name__, url_prefix="/users")

# List out all the users
@users.route("/", methods=["GET"])
def get_users():
    try:
        users = User.query.all()
        result = users_schema.dump(users)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500
    