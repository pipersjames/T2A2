from flask import Blueprint, jsonify
from main import db
from models.request_types import request_type
from schemas.request_types import request_type_schema, request_types_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from decorators.admin import admin_required

request_types = Blueprint("request_types", __name__, url_prefix="/request_types")

# List out all the request_types
@request_types.route("/", methods=["GET"])
def get_request_types():
    try:
        request_types = RequestType.query.all()
        result = request_types_schema.dump(request_types)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#return data of specific request_type using the id as input  
    
@request_types.route("/<int:request_type_id>", methods=["GET"])
def get_request_type(request_type_id: int):
    try:
        query = db.select(RequestType).filter_by(id=request_type_id)
        request_type = db.session.scalar(query)
        result = request_type_schema.dump(request_type)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#delete an existing request_type record by id    
@request_types.route("/<int:request_type_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_request_type(request_type_id: int):
    q = db.select(RequestType).filter_by(id=request_type_id)
    request_type = db.session.scalar(q)
    response = request_type_schema.dump(request_type)

    if response:
        request_type_data = {
        "name": request_type.name,
    }
        db.session.delete(request_type)
        db.session.commit()
        return jsonify(message=f"request_type {request_type.name} has been deleted successfully!")

    return jsonify(message=f"request_type '{request_type_id}' not found. No records deleted")


#create a new request_type entry
@request_types.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_request_type():
    request_type_json = request_type_schema.load(request.json)
    request_type = RequestType(**request_type_json)
    
    db.session.add(request_type)
    db.session.commit()
    
    return jsonify(request_type_schema.dump(request_type))

#patch specific sections of the request_type information depending on what is added to the json

@request_types.route("/<int:request_type_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_request_type(request_type_id: int):
    try:
        q = db.select(RequestType).filter_by(id=request_type_id)
        request_type = db.session.scalar(q)

        request_type_json = request_type_schema.load(request.json, partial=True)
        for field, value in request_type_json.request_types():
            setattr(request_type, field, value)
        db.session.commit()
        return jsonify(request_type_schema.dump(request_type))

        return jsonify(message=f"Cannot update request_type with id=`{request_type_id}`. Not found or unauthorized"), 403

    except Exception as e:
        return jsonify({"message": "An error occurred while updating the request_type", "error": str(e)}), 500