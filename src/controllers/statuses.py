from flask import Blueprint, jsonify
from main import db
from models.statuses import Status
from schemas.statuses import status_schema, statuses_schema

statuses = Blueprint("statuses", __name__, url_prefix="/statuses")

# List out all the users
@statuses.route("/", methods=["GET"])
def get_statuses():
    try:
        statuses = Status.query.all()
        result = statuses_schema.dump(statuses)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500