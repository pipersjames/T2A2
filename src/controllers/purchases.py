from flask import Blueprint, jsonify
from main import db
from models.purchases import Purchase
from schemas.purchases import purchase_schema, purchases_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from decorators.admin import admin_required

purchases = Blueprint("purchases", __name__, url_prefix="/purchases")

# List out all the purchases
@purchases.route("/", methods=["GET"])
def get_purchases():
    try:
        purchases = Purchase.query.all()
        result = purchases_schema.dump(purchases)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#return data of specific purchase using the id as input  
    
@purchases.route("/<int:purchase_id>", methods=["GET"])
def get_purchase(purchase_id: int):
    try:
        query = db.select(Purchase).filter_by(id=purchase_id)
        purchase = db.session.scalar(query)
        result = purchase_schema.dump(purchase)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#delete an existing purchase record by id    
@purchases.route("/<int:purchase_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_purchase(purchase_id: int):
    q = db.select(Purchase).filter_by(id=purchase_id)
    purchase = db.session.scalar(q)
    response = purchase_schema.dump(purchase)

    if response:
        purchase_data = {
        "name": purchase.name,
    }
        db.session.delete(purchase)
        db.session.commit()
        return jsonify(message=f"purchase {purchase.name} has been deleted successfully!")

    return jsonify(message=f"purchase '{purchase_id}' not found. No records deleted")


#create a new purchase entry
@purchases.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_purchase():
    purchase_json = purchase_schema.load(request.json)
    purchase = Purchase(**purchase_json)
    
    db.session.add(purchase)
    db.session.commit()
    
    return jsonify(purchase_schema.dump(purchase))

#patch specific sections of the purchase information depending on what is added to the json

@purchases.route("/<int:purchase_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_purchase(purchase_id: int):
    try:
        q = db.select(Purchase).filter_by(id=purchase_id)
        purchase = db.session.scalar(q)

        purchase_json = purchase_schema.load(request.json, partial=True)
        for field, value in purchase_json.items():
            setattr(purchase, field, value)
        db.session.commit()
        return jsonify(purchase_schema.dump(purchase))

        return jsonify(message=f"Cannot update purchase with id=`{purchase_id}`. Not found or unauthorized"), 403

    except Exception as e:
        return jsonify({"message": "An error occurred while updating the purchase", "error": str(e)}), 500