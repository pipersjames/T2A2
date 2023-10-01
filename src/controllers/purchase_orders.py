from flask import Blueprint
from main import db
from models.purchase_orders import PurchaseOrder
from schemas.purchase_orders import purchase_order_schema, purchase_orders_schema
from flask_jwt_extended import jwt_required
from decorators.admin import admin_required
from controllers import crud

purchase_orders = Blueprint("purchase_orders", __name__, url_prefix="/purchase_orders")

# List out all the purchase_orders - refer get_all_records in crud.py
@purchase_orders.route("/", methods=["GET"])
@jwt_required()
def get_purchase_orders():
    return crud.get_all_records(PurchaseOrder, purchase_orders_schema) 

# retuns the information related to the purchase_order by id. this is given in a integer format in the route heading- refer get_record in crud.py  
@purchase_orders.route("/<int:purchase_order_id>", methods=["GET"])
@jwt_required()
def get_purchase_order(purchase_order_id: int):
    return crud.get_record(PurchaseOrder,purchase_order_schema,purchase_order_id)

#deletes a record in the purchase_orders table by id - refer delete_record in crud.py  
@purchase_orders.route("/<int:purchase_order_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_purchase_order(purchase_order_id: int):
    return crud.delete_record(PurchaseOrder,purchase_order_schema,purchase_order_id)

#create a new purchase_order entry - refer create_new record in crud.py
@purchase_orders.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_purchase_order():
    return crud.create_new_record(PurchaseOrder, purchase_order_schema)

# used for injecting purchase order records in bulk - refer create_new_records in crud.py
@purchase_orders.route("/multiple", methods=["POST"])
@jwt_required()
@admin_required
def create_new_purchase_orders():
    return crud.create_new_records(PurchaseOrder, purchase_orders_schema)

#patches the information in the purchase_orders table - refer patch record in crud.py
@purchase_orders.route("/<int:purchase_order_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_purchase_order(purchase_order_id: int):
    return crud.patch_record(PurchaseOrder, purchase_order_schema, purchase_order_id)