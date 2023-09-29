from flask import Blueprint, jsonify
from main import db
from models.items import Item
from schemas.items import item_schema, items_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from decorators.admin import admin_required

items = Blueprint("items", __name__, url_prefix="/items")

# List out all the items
@items.route("/", methods=["GET"])
def get_items():
    try:
        items = Item.query.all()
        result = items_schema.dump(items)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#return data of specific item using the id as input  
    
@items.route("/<int:item_id>", methods=["GET"])
def get_item(item_id: int):
    try:
        query = db.select(Item).filter_by(id=item_id)
        item = db.session.scalar(query)
        result = item_schema.dump(item)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#delete an existing item record by id    
@items.route("/<int:item_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_item(item_id: int):
    q = db.select(Item).filter_by(id=item_id)
    item = db.session.scalar(q)
    response = item_schema.dump(item)

    if response:
        item_data = {
        "name": item.name,
    }
        db.session.delete(item)
        db.session.commit()
        return jsonify(message=f"item {item.name} has been deleted successfully!")

    return jsonify(message=f"item '{item_id}' not found. No records deleted")


#create a new item entry
@items.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_item():
    item_json = item_schema.load(request.json)
    item = Item(**item_json)
    
    db.session.add(item)
    db.session.commit()
    
    return jsonify(item_schema.dump(item))

#patch specific sections of the item information depending on what is added to the json

@items.route("/<int:item_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_item(item_id: int):
    try:
        q = db.select(Item).filter_by(id=item_id)
        item = db.session.scalar(q)

        item_json = item_schema.load(request.json, partial=True)
        for field, value in item_json.items():
            setattr(item, field, value)
        db.session.commit()
        return jsonify(item_schema.dump(item))

        return jsonify(message=f"Cannot update item with id=`{item_id}`. Not found or unauthorized"), 403

    except Exception as e:
        return jsonify({"message": "An error occurred while updating the item", "error": str(e)}), 500