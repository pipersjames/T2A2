from main import ma
from marshmallow import fields

class RequestSchema(ma.Schema):
    class Meta:
        fields = "id", "request_type_id", "status_id", "user_id", "comment", "issue_qty", "docket_number", "created_at", "completion_comment"


request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)