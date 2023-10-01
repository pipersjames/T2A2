from flask import Blueprint, jsonify, request
from main import db, bcrypt
from models.users import User
from schemas.users import user_schema, users_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from decorators.admin import admin_required
from controllers import crud

users = Blueprint("users", __name__, url_prefix="/users")

   
# List out all the users - refer get_all_records in crud.py - admin protected (refer admin_required in decorators)
@users.route("/all", methods=["GET"])
@jwt_required()
@admin_required
def get_users():
    return crud.get_all_records(User,users_schema) 

# retuns the information related to the user by id. this is given in a integer format in the route heading- refer get_record in crud.py - admin protected (refer admin_required in decorators)

@users.route("/<int:user_id>", methods=["GET"])
@jwt_required()
@admin_required
def get_department(user_id: int):
    return crud.get_record(User,user_schema,user_id)
    
#get current user data to return a personal record

@users.route("/", methods=["GET"])
@jwt_required()
def get_current_user():
    try:
        #check identity in the token and store in variable
        identity = get_jwt_identity()
        # query the user table to match the current token identity
        query = db.select(User).filter_by(email=identity)
        # store the user data in a variable
        user = db.session.scalar(query)
        # create a dump for the client 
        result = user_schema.dump(user)
        # return the dump
        return jsonify(result), 200
    # handle the errors
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500
    

#deletes a record in the users table by id - refer delete_record in crud.py - admin protected (refer admin_required in decorators) 
@users.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_user(user_id: int):
    return crud.delete_record(User,user_schema,user_id)


#create a new user entry - refer create_new record in crud.py - admin protected (refer admin_required in decorators) 
@users.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_user():
    return crud.create_new_record(User, user_schema)

#update user data - jwt required 

#patches the information in the users table - refer patch record in crud.py - admin protected (refer admin_required in decorators)
@users.route("/<int:user_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_user(user_id: int):
    return crud.patch_record(User, user_schema, user_id)
    


