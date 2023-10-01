from flask import Blueprint
from main import db
from models.suppliers import Supplier
from schemas.suppliers import supplier_schema, suppliers_schema
from flask_jwt_extended import jwt_required
from decorators.admin import admin_required
from controllers import crud

suppliers = Blueprint("suppliers", __name__, url_prefix="/suppliers")

# List out all the suppliers - refer get_all_records in crud.py
@suppliers.route("/", methods=["GET"])
def get_suppliers():
    return crud.get_all_records(Supplier,suppliers_schema) 

# retuns the information related to the supplier by id. this is given in a integer format in the route heading- refer get_record in crud.py  
@suppliers.route("/<int:supplier_id>", methods=["GET"])
def get_supplier(supplier_id: int):
    return crud.get_record(Supplier,supplier_schema,supplier_id)

#deletes a record in the suppliers table by id - refer delete_record in crud.py  
@suppliers.route("/<int:supplier_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_supplier(supplier_id: int):
    return crud.delete_record(Supplier,supplier_schema,supplier_id)

#create a new supplier entry - refer create_new record in crud.py
@suppliers.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_supplier():
    return crud.create_new_record(Supplier, supplier_schema)

#patches the information in the suppliers table - refer patch record in crud.py
@suppliers.route("/<int:supplier_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_supplier(supplier_id: int):
    return crud.patch_record(Supplier, supplier_schema, supplier_id)