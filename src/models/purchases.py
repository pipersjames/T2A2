from main import db

class Purchase(db.Model):
    __tablename__ = "purchases"
    
    id = db.Column(db.Integer, primary_key=True)
    
    po_number = db.Column(db.Integer)
    backorder_suffix = db.Column(db.String(length=2), nullable=True)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"))
    supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"))
    
    #relationships
    
    items = db.relationship(
    "Item",
    secondary="purchase_orders",
    back_populates="purchases"
)

