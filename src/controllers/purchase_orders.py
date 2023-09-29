from flask import Blueprint, jsonify
from main import db
from models.purchase_orders import PurchaseOrder
from schemas.purchase_orders import purchase_order_schema, purchase_orders_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from decorators.admin import admin_required

purchase_orders = Blueprint("purchase_orders", __name__, url_prefix="/purchase_orders")

# List out all the purchase_orders
@purchase_orders.route("/", methods=["GET"])
def get_purchase_orders():
    try:
        purchase_orders = PurchaseOrder.query.all()
        result = purchase_orders_schema.dump(purchase_orders)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#return data of specific purchase_order using the id as input  
    
@purchase_orders.route("/<int:purchase_order_id>", methods=["GET"])
def get_purchase_order(purchase_order_id: int):
    try:
        query = db.select(PurchaseOrder).filter_by(id=purchase_order_id)
        purchase_order = db.session.scalar(query)
        result = purchase_order_schema.dump(purchase_order)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#delete an existing purchase_order record by id    
@purchase_orders.route("/<int:purchase_order_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_purchase_order(purchase_order_id: int):
    q = db.select(PurchaseOrder).filter_by(id=purchase_order_id)
    purchase_order = db.session.scalar(q)
    response = purchase_order_schema.dump(purchase_order)

    if response:
        purchase_order_data = {
        "name": purchase_order.name,
    }
        db.session.delete(purchase_order)
        db.session.commit()
        return jsonify(message=f"purchase_order {purchase_order.name} has been deleted successfully!")

    return jsonify(message=f"purchase_order '{purchase_order_id}' not found. No records deleted")


#create a new purchase_order entry
@purchase_orders.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_purchase_order():
    purchase_order_json = purchase_order_schema.load(request.json)
    purchase_order = PurchaseOrder(**purchase_order_json)
    
    db.session.add(purchase_order)
    db.session.commit()
    
    return jsonify(purchase_order_schema.dump(purchase_order))

#patch specific sections of the purchase_order information depending on what is added to the json

@purchase_orders.route("/<int:purchase_order_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_purchase_order(purchase_order_id: int):
    try:
        q = db.select(PurchaseOrder).filter_by(id=purchase_order_id)
        purchase_order = db.session.scalar(q)

        purchase_order_json = purchase_order_schema.load(request.json, partial=True)
        for field, value in purchase_order_json.purchase_orders():
            setattr(purchase_order, field, value)
        db.session.commit()
        return jsonify(purchase_order_schema.dump(purchase_order))

        return jsonify(message=f"Cannot update purchase_order with id=`{purchase_order_id}`. Not found or unauthorized"), 403

    except Exception as e:
        return jsonify({"message": "An error occurred while updating the purchase_order", "error": str(e)}), 500