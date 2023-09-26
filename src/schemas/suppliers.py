from main import ma
from marshmallow import fields

class SupplierSchema(ma.Schema):
    class Meta:
        fields = "id", "name", "contact_email", "claim_policy", "lead_time"


supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)