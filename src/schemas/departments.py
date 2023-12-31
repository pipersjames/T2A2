from main import ma
from marshmallow import fields

class DepartmentSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = (
            "id",
            "name", 
            "location", 
            "open_hours", 
            "warehouse_number"
        )
        load_only = ["id"]

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)