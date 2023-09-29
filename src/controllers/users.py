from flask import Blueprint, jsonify, request
from main import db, bcrypt
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
    
#get current user data

@users.route("/", methods=["GET"])
@jwt_required()
def get_current_user():
    try:
        identity = get_jwt_identity()
        query = db.select(User).filter_by(email=identity)
        user = db.session.scalar(query)
        result = user_schema.dump(user)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500
    
# delete a user based on id - admin only
    
@users.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_user(user_id: int):
    q = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(q)
    response = user_schema.dump(user)

    if response:
        user_data = {
        "first_name": user.first_name,
        "second_name": user.second_name,
    }
        db.session.delete(user)
        db.session.commit()
        return jsonify(message=f"User {user.second_name, user.first_name} has been deleted successfully!")

    return jsonify(message=f"User '{user_id}' not found. No records deleted")

# create a new user - admin only

@users.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_user():
    user_json = user_schema.load(request.json)
    user = User(
        **{
            "first_name": user_json["first_name"],
            "second_name": user_json["second_name"],
            "email": user_json["email"],
            "password": bcrypt.generate_password_hash(user_json["password"]).decode("utf"),
            "phone_number": user_json["phone_number"],
            "department_id": user_json["department_id"], 
            "admin": user_json["admin"],
        }
    )
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify(user_schema.dump(user))

#update user data - jwt required 

@users.route("/<int:user_id>", methods=["PATCH"])
@jwt_required()
def patch_user(user_id: int):
    try:
        current_user_email = get_jwt_identity()

        q = db.select(User).filter_by(id=user_id)
        user = db.session.scalar(q)

        if user and current_user_email == user.email:
            user_json = user_schema.load(request.json, partial=True)
            for field, value in user_json.items():
                setattr(user, field, value)
            db.session.commit()
            return jsonify(user_schema.dump(user))

        return jsonify(message=f"Cannot update user with id=`{user_id}`. Not found or unauthorized"), 403

    except Exception as e:
        return jsonify({"message": "An error occurred while updating the user", "error": str(e)}), 500
    


