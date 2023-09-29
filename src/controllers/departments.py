from flask import Blueprint, jsonify
from main import db
from models.departments import Department
from schemas.departments import department_schema, departments_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from decorators.admin import admin_required

departments = Blueprint("departments", __name__, url_prefix="/departments")

# List out all the departments
@departments.route("/", methods=["GET"])
def get_departments():
    try:
        departments = Department.query.all()
        result = departments_schema.dump(departments)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#return data of specific department using the id as input  
    
@departments.route("/<int:department_id>", methods=["GET"])
def get_department(department_id: int):
    try:
        query = db.select(Department).filter_by(id=department_id)
        department = db.session.scalar(query)
        result = department_schema.dump(department)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching users", "error": str(e)}), 500

#delete an existing department record by id    
@departments.route("/<int:department_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_department(department_id: int):
    q = db.select(Department).filter_by(id=department_id)
    department = db.session.scalar(q)
    response = department_schema.dump(department)

    if response:
        department_data = {
        "name": department.name,
    }
        db.session.delete(department)
        db.session.commit()
        return jsonify(message=f"department {department.name} has been deleted successfully!")

    return jsonify(message=f"department '{department_id}' not found. No records deleted")


#create a new department entry
@departments.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_new_department():
    department_json = department_schema.load(request.json)
    department = Department(**department_json)
    
    db.session.add(department)
    db.session.commit()
    
    return jsonify(department_schema.dump(department))

#patch specific sections of the department information depending on what is added to the json

@departments.route("/<int:department_id>", methods=["PATCH"])
@jwt_required()
@admin_required
def patch_department(department_id: int):
    try:
        q = db.select(Department).filter_by(id=department_id)
        department = db.session.scalar(q)

        department_json = department_schema.load(request.json, partial=True)
        for field, value in department_json.departments():
            setattr(department, field, value)
        db.session.commit()
        return jsonify(department_schema.dump(department))

        return jsonify(message=f"Cannot update department with id=`{department_id}`. Not found or unauthorized"), 403

    except Exception as e:
        return jsonify({"message": "An error occurred while updating the department", "error": str(e)}), 500