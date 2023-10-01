from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import create_access_token
from datetime import timedelta
from main import db, bcrypt
from models.users import User
from schemas.users import user_schema
from werkzeug.exceptions import BadRequest

auths = Blueprint("auth", __name__, url_prefix="/auths")

# creates a new user and provides a token for the current session. admin field intentionally excluded to prevent new users from making themsevles one. 
@auths.route("/register", methods=["POST"])
def register_user():
    #try block to handle errors, in particular the case where additional fields or less than are provided.
    try:
        # loads the json provided by the client
        user_json = user_schema.load(request.json)
        # makes a new instance given the parameters set below
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
        # add the session
        db.session.add(user)
        # commit changes
        db.session.commit()
        # generate a token for the new user
        access_token = create_access_token(identity=user_json["email"])
        # return the token to the client
        return jsonify({"token": access_token})
    except Exception as e:
            return jsonify({"message": "An error occured", "error": str(e)}), 500
        

# Takes the user email and password as input. Checks the users table to look for a match and then generates a token for the current sesssion.
@auths.route("/login", methods=["POST"])
def login_user():
    # error handler block
    try:
        # loads the email and passord from the input json    
        email = request.json.get("email")
        password = request.json.get("password")

        # Query the database to find the user by email
        query = db.select(User).filter_by(email=email)
        user = db.session.scalar(query)

        # if case to prevent login if credentials don't match
        if not user or not bcrypt.check_password_hash(user.password, password):
            return abort(401, description="Incorrect email or password. Please try again")
        # set the token timer to 1 hours.
        expiration_time = timedelta(hours=1)
        # gemerate tje token
        access_token = create_access_token(identity=user.email, expires_delta=expiration_time)

        return jsonify({"token": access_token})
    
    except Exception as e:
            return jsonify({"message": "An error occured", "error": str(e)}), 500

