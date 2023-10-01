from main import ma
from marshmallow import fields
from schemas.items import items_schema

class PurchaseSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = (
            "id",
            "po_number",
            "backorder_suffix",
            "department_id",
            "supplier_id",
            "items",
        )

        load_only = ['id']
        
    items = fields.Nested(items_schema)


purchase_schema = PurchaseSchema()
purchases_schema = PurchaseSchema(many=True)
