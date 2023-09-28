from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# from sqlalchemy import text

from main import db, bycrypt
from models.users import User
from schemas.users import user_schema

auths = Blueprint("auth", __name__, url_prefix="/auths")

@auths.route("/register", methods=["POST"])
def register_user():
    user_json = user_schema.load(request.json)
    user = User(
        **{
            "first_name": user_json["first_name"],
            "second_name": user_json["second_name"],
            "email": user_json["email"],
            "password": bycrypt.generate_password_hash(user_json["password"]).decode("utf"),
            "phone_number": user_json["phone_number"],
            "department_id": user_json["department_id"], 
        }
    )
    db.session.add(user)
    db.session.commit()
    
    access_token = create_access_token(identity=user_json["email"])

    return jsonify({"token": access_token})
    
# @auths.route('/check', methods=["GET"])
# def check_db_connection():
#     try:
#         with db.session() as session:
#             session.execute(text('SELECT 1'))
#         return jsonify(message='Database connection is working.')
#     except Exception as e:
#         return jsonify(message='Database connection error: {}'.format(str(e))), 500