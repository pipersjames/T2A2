from flask import Blueprint, jsonify
from main import db
from models.suppliers import Supplier
from schemas.suppliers import supplier_schema, suppliers_schema

suppliers = Blueprint("suppliers", __name__, url_prefix="/suppliers")

# List out all the users
@suppliers.route("/", methods=["GET"])
def get_suppliers():
    try:
        suppliers = Supplier.query.all()
        result = suppliers_schema.dump(suppliers)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500