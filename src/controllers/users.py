from flask import Blueprint, jsonify
from main import db
from models.users import User
from schemas.users import user_schema, users_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from decorators.admin import admin_required

users = Blueprint("users", __name__, url_prefix="/users")

# returns a list out all the users - restricted to admin
@users.route("/all", methods=["GET"])
@jwt_required()
@admin_required
def get_users():
    try:
        users = User.query.all()
        result = users_schema.dump(users)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#returns user data by id - restricted to admin

@users.route("/<int:user_id>", methods=["GET"])
@jwt_required()
@admin_required
def get_user(user_id: int):
    try:
        query = db.select(User).filter_by(id=user_id)
        user = db.session.scalar(query)
        result = user_schema.dump(user)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500


    