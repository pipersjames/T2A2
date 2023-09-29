from main import ma
from marshmallow import fields

class ItemSchema(ma.Schema):
    class Meta:
        fields = "id", "internal_code", "supp_code", "description", "supp_id"

        load_only = ["supp_id"]


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)