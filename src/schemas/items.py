from main import ma
from marshmallow import fields
from schemas.suppliers import supplier_schema

class ItemSchema(ma.Schema):
    class Meta: 
        ordered = True
        fields = (
            "id",
            "internal_code",
            "supp_code",
            "description",
            "supp_id",
            "supplier"
        )
        
        exclude = ("supplier.id",)
        load_only = ["id","supp_id"]
        
    supplier = fields.Nested(supplier_schema, ordered=True)


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)