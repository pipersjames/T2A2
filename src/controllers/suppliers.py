from flask import Blueprint, jsonify
from main import db
from models.suppliers import Supplier
from schemas.suppliers import supplier_schema, suppliers_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from decorators.admin import admin_required

suppliers = Blueprint("suppliers", __name__, url_prefix="/suppliers")

# List out all the suppliers
@suppliers.route("/", methods=["GET"])
def get_suppliers():
    try:
        suppliers = Supplier.query.all()
        result = suppliers_schema.dump(suppliers)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#return data of specific supplier using the id as input  
    
@suppliers.route("/<int:supplier_id>", methods=["GET"])
def get_supplier(supplier_id: int):
    try:
        query = db.select(Supplier).filter_by(id=supplier_id)
        supplier = db.session.scalar(query)
        result = supplier_schema.dump(supplier)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#delete an existing supplier record by id    
@suppliers.route("/<int:supplier_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_supplier(supplier_id: int):
    q = db.select(supplier).filter_by(id=supplier_id)
    supplier = db.session.scalar(q)
    response = supplier_schema.dump(supplier)

    if response:
        supplier_data = {
        "name": supplier.name,
    }
        db.session.delete(supplier)
        db.session.commit()
        return jsonify(message=f"supplier {supplier.name} has been deleted successfully!")

    return jsonify(message=f"supplier '{supplier_id}' not found. No records deleted")


#create a new supplier entry
@suppliers.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_supplier():
    supplier_json = supplier_schema.load(request.json)
    supplier = Supplier(**supplier_json)
    
    db.session.add(supplier)
    db.session.commit()
    
    return jsonify(supplier_schema.dump(supplier))

#patch specific sections of the supplier information depending on what is added to the json

@suppliers.route("/<int:supplier_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_supplier(supplier_id: int):
    try:
        q = db.select(supplier).filter_by(id=supplier_id)
        supplier = db.session.scalar(q)

        supplier_json = supplier_schema.load(request.json, partial=True)
        for field, value in supplier_json.items():
            setattr(supplier, field, value)
        db.session.commit()
        return jsonify(supplier_schema.dump(supplier))

        return jsonify(message=f"Cannot update supplier with id=`{supplier_id}`. Not found or unauthorized"), 403

    except Exception as e:
        return jsonify({"message": "An error occurred while updating the supplier", "error": str(e)}), 500