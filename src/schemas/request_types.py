from main import ma
from marshmallow import fields

class RequestTypeSchema(ma.Schema):
    class Meta:
        fields = "id", "description"


request_type_schema = RequestTypeSchema()
request_types_schema = RequestTypeSchema(many=True)