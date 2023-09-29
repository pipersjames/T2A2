from flask import Blueprint, jsonify
from main import db
from models.statuses import Status
from schemas.statuses import status_schema, statuses_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from decorators.admin import admin_required

statuses = Blueprint("statuses", __name__, url_prefix="/statuses")

# List out all the statuss
@statuses.route("/", methods=["GET"])
def get_statuses():
    try:
        statuses = Status.query.all()
        result = statuses_schema.dump(statuses)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#return data of specific status using the id as input  
    
@statuses.route("/<int:status_id>", methods=["GET"])
def get_status(status_id: int):
    try:
        query = db.select(Status).filter_by(id=status_id)
        status = db.session.scalar(query)
        result = status_schema.dump(status)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#delete an existing status record by id    
@statuses.route("/<int:status_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_status(status_id: int):
    q = db.select(Status).filter_by(id=status_id)
    status = db.session.scalar(q)
    response = status_schema.dump(status)

    if response:
        status_data = {
        "name": status.name,
    }
        db.session.delete(Status)
        db.session.commit()
        return jsonify(message=f"status {status.name} has been deleted successfully!")

    return jsonify(message=f"status '{status_id}' not found. No records deleted")


#create a new status entry
@statuses.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_status():
    status_json = status_schema.load(request.json)
    status = Status(**status_json)
    
    db.session.add(status)
    db.session.commit()
    
    return jsonify(status_schema.dump(status))

#patch specific sections of the status information depending on what is added to the json

@statuses.route("/<int:status_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_status(status_id: int):
    try:
        q = db.select(Status).filter_by(id=status_id)
        status = db.session.scalar(q)

        status_json = status_schema.load(request.json, partial=True)
        for field, value in status_json.statuses():
            setattr(status, field, value)
        db.session.commit()
        return jsonify(status_schema.dump(status))

        return jsonify(message=f"Cannot update status with id=`{status_id}`. Not found or unauthorized"), 403

    except Exception as e:
        return jsonify({"message": "An error occurred while updating the status", "error": str(e)}), 500