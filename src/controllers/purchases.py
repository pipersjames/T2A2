from flask import Blueprint
from main import db
from models.purchases import Purchase
from schemas.purchases import purchase_schema, purchases_schema
from flask_jwt_extended import jwt_required
from decorators.admin import admin_required
from controllers import crud


purchases = Blueprint("purchases", __name__, url_prefix="/purchases")

# List out all the purchases - refer get_all_records in crud.py
@purchases.route("/", methods=["GET"])
def get_purchases():
    return crud.get_all_records(Purchase,purchases_schema) 

# retuns the information related to the purchase by id. this is given in a integer format in the route heading- refer get_record in crud.py  
@purchases.route("/<int:purchase_id>", methods=["GET"])
def get_purchase(purchase_id: int):
    return crud.get_record(Purchase,purchase_schema,purchase_id)

#deletes a record in the purchases table by id - refer delete_record in crud.py  
@purchases.route("/<int:purchase_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_purchase(purchase_id: int):
    return crud.delete_record(Purchase,purchase_schema,purchase_id)

#create a new purchase entry - refer create_new record in crud.py
@purchases.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_purchase():
    return crud.create_new_record(Purchase, purchase_schema)


# used for injecting purchase records in bulk - refer create_new_records in crud.py
@purchases.route("/multiple", methods=["POST"])
@jwt_required()
@admin_required
def create_new_purchases():
    return crud.create_new_records(Purchase, purchases_schema)

#patches the information in the purchases table - refer patch record in crud.py
@purchases.route("/<int:purchase_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_purchase(purchase_id: int):
    return crud.patch_record(Purchase, purchase_schema, purchase_id)