from flask import Blueprint, jsonify
from main import db
from models.requests import Request
from schemas.requests import request_schema, requests_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from decorators.admin import admin_required

requests = Blueprint("requests", __name__, url_prefix="/requests")

# List out all the requests
@requests.route("/", methods=["GET"])
def get_requests():
    try:
        requests = Request.query.all()
        result = requests_schema.dump(requests)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#return data of specific request using the id as input  
    
@requests.route("/<int:request_id>", methods=["GET"])
def get_request(request_id: int):
    try:
        query = db.select(Request).filter_by(id=request_id)
        request = db.session.scalar(query)
        result = request_schema.dump(request)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#delete an existing request record by id    
@requests.route("/<int:request_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_request(request_id: int):
    q = db.select(Request).filter_by(id=request_id)
    request = db.session.scalar(q)
    response = request_schema.dump(request)

    if response:
        request_data = {
        "name": request.name,
    }
        db.session.delete(request)
        db.session.commit()
        return jsonify(message=f"request {request.name} has been deleted successfully!")

    return jsonify(message=f"request '{request_id}' not found. No records deleted")


#create a new request entry
@requests.route("/", methods=["POST"])
def create_new_request():
    request_json = request_schema.load(request.json)
    request = Request(**request_json)
    
    db.session.add(request)
    db.session.commit()
    
    return jsonify(request_schema.dump(request))

#patch specific sections of the request information depending on what is added to the json

@requests.route("/<int:request_id>", methods=["PATCH"])
def patch_request(request_id: int):
    try:
        q = db.select(Request).filter_by(id=request_id)
        request = db.session.scalar(q)

        request_json = request_schema.load(request.json, partial=True)
        for field, value in request_json.requests():
            setattr(request, field, value)
        db.session.commit()
        return jsonify(request_schema.dump(request))

        return jsonify(message=f"Cannot update request with id=`{request_id}`. Not found or unauthorized"), 403

    except Exception as e:
        return jsonify({"message": "An error occurred while updating the request", "error": str(e)}), 500