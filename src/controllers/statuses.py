from flask import Blueprint
from main import db
from models.statuses import Status
from schemas.statuses import status_schema, statuses_schema
from flask_jwt_extended import jwt_required
from decorators.admin import admin_required
from controllers import crud

statuses = Blueprint("statuses", __name__, url_prefix="/statuses")

# List out all the status - refer get_all_records in crud.py
@statuses.route("/", methods=["GET"])
@jwt_required()
def get_all_status():
    return crud.get_all_records(Status, statuses_schema) 

# retuns the information related to the status by id. this is given in a integer format in the route heading- refer get_record in crud.py  
@statuses.route("/<int:status_id>", methods=["GET"])
@jwt_required()
def get_status(status_id: int):
    return crud.get_record(Status, status_schema,status_id)

#deletes a record in the status table by id - refer delete_record in crud.py  
@statuses.route("/<int:statusid>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_status(status_id: int):
    return crud.delete_record(Status,status_schema,status_id)

#create a new status entry - refer create_new record in crud.py
@statuses.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_status():
    return crud.create_new_record(Status, status_schema)

#patches the information in the status table - refer patch record in crud.py
@statuses.route("/<int:statusid>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_status(status_id: int):
    return crud.patch_record(Status, status_schema, status_id)