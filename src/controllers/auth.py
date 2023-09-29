from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

from main import db, bcrypt
from models.users import User
from schemas.users import user_schema

auths = Blueprint("auth", __name__, url_prefix="/auths")

# needs to handle already registered user gracefully
@auths.route("/register", methods=["POST"])
def register_user():
    user_json = user_schema.load(request.json)
    user = User(
        **{
            "first_name": user_json["first_name"],
            "second_name": user_json["second_name"],
            "email": user_json["email"],
            "password": bcrypt.generate_password_hash(user_json["password"]).decode("utf"),
            "phone_number": user_json["phone_number"],
            "department_id": user_json["department_id"], 
        }
    )
    db.session.add(user)
    db.session.commit()
    
    access_token = create_access_token(identity=user_json["email"])

    return jsonify({"token": access_token})


@auths.route("/check-session", methods=["POST"])
@jwt_required()
def login_check():
    email_identity = get_jwt_identity()
    
    query = db.select(User).filter_by(email=email_identity)
    user = db.session.scalar(query)
    
    user_data = {
        "first_name": user.first_name,
        "second_name": user.second_name,
        "email": user.email
    }
    
    return jsonify(logged_in_as=user_data), 200


@auths.route("/login", methods=["POST"])
def login_user():
    email = request.json.get("email")
    password = request.json.get("password")

    # Query the database to find the user by email
    query = db.select(User).filter_by(email=email)
    user = db.session.scalar(query)

    if not user or not bcrypt.check_password_hash(user.password, password):
        return abort(401, description="Incorrect email or password. Please try again")
    # added additional time to the token - consider refreshing token during use
    expiration_time = timedelta(hours=1)
    # If the user exists and the password is correct, generate a JWT
    access_token = create_access_token(identity=user.email, expires_delta=expiration_time)

    # Return the token to the client
    return jsonify({"token": access_token})

