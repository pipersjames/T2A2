from main import ma
from marshmallow import fields

class StatusSchema(ma.Schema):
    class Meta:
        fields = "id", "description"


status_schema = StatusSchema()
statuses_schema = StatusSchema(many=True)