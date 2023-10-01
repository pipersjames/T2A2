from flask import Blueprint
from models.items import Item
from schemas.items import item_schema, items_schema
from flask_jwt_extended import jwt_required
from decorators.admin import admin_required
from controllers import crud

items = Blueprint("items", __name__, url_prefix="/items")

# List out all the items - refer get_all_records in crud.py
@items.route("/", methods=["GET"])
@jwt_required()
def get_items():
    return crud.get_all_records(Item, items_schema) 

# retuns the information related to the item by id. this is given in a integer format in the route heading- refer get_record in crud.py  
@items.route("/<int:item_id>", methods=["GET"])
@jwt_required()
def get_item(item_id: int):
    return crud.get_record(Item,item_schema,item_id)

#deletes a record in the items table by id - refer delete_record in crud.py  
@items.route("/<int:item_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_item(item_id: int):
    return crud.delete_record(Item,item_schema,item_id)

#create a new item entry - refer create_new_record in crud.py
@items.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_item():
    return crud.create_new_record(Item, item_schema)

# used for injecting item records in bulk - refer create_new_records in crud.py
@items.route("/multiple", methods=["POST"])
@jwt_required()
@admin_required
def create_new_items():
    return crud.create_new_records(Item, items_schema)

#patches the information in the items table - refer patch record in crud.py
@items.route("/<int:item_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_item(item_id: int):
    return crud.patch_record(Item, item_schema, item_id)