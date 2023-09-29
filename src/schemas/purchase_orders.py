from main import ma
from marshmallow import fields

class PurchaseOrderSchema(ma.Schema):
    class Meta:
        fields = (
            "purchase_id",
            "item_id",
            "order_date",
            "received date",
            "qty",
        )


purchase_order_schema = PurchaseOrderSchema()
purchase_orders_schema = PurchaseOrderSchema(many=True)