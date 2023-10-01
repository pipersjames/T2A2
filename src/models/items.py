from main import db

class Item(db.Model):
    __tablename__ = "items"
    
    id = db.Column(db.Integer, primary_key=True)
    
    internal_code = db.Column(db.String(length=20), unique=True, nullable=False)
    supp_code = db.Column(db.String(length=20), nullable=False)
    description = db.Column(db.String(length=40), nullable=True)
    supp_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"), nullable=False)
   
   
   
    purchase_orders = db.relationship(
        "PurchaseOrder",
        back_populates="item",
        cascade="all, delete"
    )
    
    supplier = db.relationship(
        "Supplier",
        back_populates="items"
    )