from main import ma
from marshmallow import fields

class DepartmentSchema(ma.Schema):
    class Meta:
        fields = "id", "location", "open_hours", "warehouse_number"


department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)