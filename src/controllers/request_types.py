from flask import Blueprint
from main import db
from models.request_types import RequestType
from schemas.request_types import request_type_schema, request_types_schema
from flask_jwt_extended import jwt_required
from decorators.admin import admin_required
from controllers import crud

request_types = Blueprint("request_types", __name__, url_prefix="/request_types")

# List out all the request_types - refer get_all_records in crud.py
@request_types.route("/", methods=["GET"])
def get_request_types():
    return crud.get_all_records(RequestType,request_types_schema) 

# retuns the information related to the request_type by id. this is given in a integer format in the route heading- refer get_record in crud.py  
@request_types.route("/<int:request_type_id>", methods=["GET"])
def get_request_type(request_type_id: int):
    return crud.get_record(RequestType,request_type_schema,request_type_id)

#deletes a record in the request_types table by id - refer delete_record in crud.py  
@request_types.route("/<int:request_type_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_request_type(request_type_id: int):
    return crud.delete_record(RequestType,request_type_schema,request_type_id)

#create a new request_type entry - refer create_new record in crud.py
@request_types.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_request_type():
    return crud.create_new_record(RequestType, request_type_schema)

#patches the information in the request_types table - refer patch record in crud.py
@request_types.route("/<int:request_type_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_request_type(request_type_id: int):
    return crud.patch_record(RequestType, request_type_schema, request_type_id)