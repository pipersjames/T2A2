from main import ma
from marshmallow import fields
from schemas.request_types import request_type_schema
from schemas.statuses import status_schema
from schemas.users import user_schema
from schemas.purchase_orders import purchase_orders_schema

class RequestSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = (
            "id",
            "purchase_order_id",
            #"item_id",
            "request_type_id",
            "status_id", 
            "user_id",
            "comment",
            "issue_qty", 
            "docket_number",
            "created_at",
            "completion_comment",
            "request_type",
            "status",
            "user",
            "purchase",
        )
        
        load_only = ["request_type_id", "status_type_id", "status_id", "purchase_order_id","item_id"]

    request_type = fields.Nested(request_type_schema, only=("description",))
    status = fields.Nested(status_schema, only=("description",))
    user = fields.Nested(user_schema, exclude=("id",))
    purchase = fields.Nested(purchase_orders_schema)
    
request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)