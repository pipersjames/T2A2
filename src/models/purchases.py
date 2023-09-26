from main import db

class Purchase(db.Model):
    __tablename__ = "purchases"
    
    id = db.Column(db.Integer, primary_key=True)
    
    po_number = db.Column(db.Integer)
    backorder_suffix = db.Column(db.Integer(length=2))
    department_id = db.Column(db.Integer, db.Foreignkey("departments.id"))
    supplier_id = db.Column(db.Integer, db.Foreignkey("suppliers.id"))
    
    #relationships
    
    items = db.relationship(
    "Item",
    secondary="purchase_orders",
    back_populates="purchases"
)

