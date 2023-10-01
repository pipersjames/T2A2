from flask import Blueprint
from models.departments import Department
from schemas.departments import department_schema, departments_schema
from flask_jwt_extended import jwt_required
from decorators.admin import admin_required
from controllers import crud


departments = Blueprint("departments", __name__, url_prefix="/departments")

# List out all the departments - refer get_all_records in crud.py
@departments.route("/", methods=["GET"])
def get_departments():
    return crud.get_all_records(Department,departments_schema) 

# retuns the information related to the department by id. this is given in a integer format in the route heading- refer get_record in crud.py  
@departments.route("/<int:department_id>", methods=["GET"])
def get_department(department_id: int):
    return crud.get_record(Department,department_schema,department_id)

#deletes a record in the departments table by id - refer delete_record in crud.py  
@departments.route("/<int:department_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_department(department_id: int):
    return crud.delete_record(Department,department_schema,department_id)

#create a new department entry - refer create_new record in crud.py
@departments.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_department():
    return crud.create_new_record(Department, department_schema)

#patches the information in the departments table - refer patch record in crud.py
@departments.route("/<int:department_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_department(department_id: int):
    return crud.patch_record(Department, department_schema, department_id)