from flask import Blueprint
from main import db
from models.requests import Request
from schemas.requests import request_schema, requests_schema
from flask_jwt_extended import jwt_required
from decorators.admin import admin_required
from controllers import crud

requests = Blueprint("requests", __name__, url_prefix="/requests")







# List out all the requests - refer get_all_records in crud.py
@requests.route("/", methods=["GET"])
def get_requests():
     return crud.get_all_records(Request,requests_schema) 

# retuns the information related to the request by id. this is given in a integer format in the route heading- refer get_record in crud.py  
@requests.route("/<int:request_id>", methods=["GET"])
def get_request(request_id: int):
    return crud.get_record(Request,request_schema,request_id)

#deletes a record in the requests table by id - refer delete_record in crud.py  
@requests.route("/<int:request_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_request(request_id: int):
    return crud.delete_record(Request,request_schema,request_id)

#create a new request entry - refer create_new record in crud.py
@requests.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_request():
    return crud.create_new_record(Request, request_schema)

#patches the information in the requests table - refer patch record in crud.py
@requests.route("/<int:request_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_request(request_id: int):
    return crud.patch_record(Request, request_schema, request_id)