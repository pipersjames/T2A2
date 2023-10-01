from main import ma
from marshmallow import fields
from schemas.items import item_schema
from schemas.purchases import purchase_schema

class PurchaseOrderSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = (
            "id",
            "purchase_id",
            "item_id",
            "purchase",
            "item",
            "order_date",
            "received_date",
            "qty",
        )
        exclude = ("item.id", "purchase.id", "purchase.supplier_id", "purchase.department_id","item.supplier")
        load_only = ["item_id","purchase_id"]
        
    item = fields.Nested(item_schema, ordered=True)
    purchase = fields.Nested(purchase_schema, ordered=True)

purchase_order_schema = PurchaseOrderSchema()
purchase_orders_schema = PurchaseOrderSchema(many=True)