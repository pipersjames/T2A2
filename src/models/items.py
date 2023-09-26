from main import db

class Item(db.Model):
    __tablename__ = "items"
    
    id = db.Column(db.Integer, primary_key=True)
    
    internal_code = db.Column(db.Integer)
    supp_code = db.Column(db.email)
    description = db.Column(db.Integer(length=2))
    supp_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"))
    
    supplier = db.relationship(
        "Supplier",
        back_populates="items"
    )
    
    purchases = db.relationship(
    "Purchase",
    secondary="purchase_orders",
    back_populates="items"
)