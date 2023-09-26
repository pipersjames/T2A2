from main import ma
from marshmallow import fields

class PurchaseSchema(ma.Schema):
    class Meta:
        fields = "id", "purchase_id", "item_id", "order_date", "received_date", "qty"

        load_only = ['purchase_id', "supp_id"]


purchase_schema = PurchaseSchema()
purchases_schema = PurchaseSchema(many=True)