from main import ma
from marshmallow import fields

class SupplierSchema(ma.Schema):
    ordered = True
    class Meta:
        fields = (
            "id",
            "name",
            "contact_email",
            "claim_policy",
            "lead_time"
        )

        load_only = ["id"]

supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)