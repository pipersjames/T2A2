from main import db
from sqlalchemy import UniqueConstraint 

class Purchase(db.Model):
    __tablename__ = "purchases"
    
    id = db.Column(db.Integer, primary_key=True)
    
    po_number = db.Column(db.Integer)
    backorder_suffix = db.Column(db.String(length=2), default="A")
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"))
    supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"))
    
    #contraint to ensure that no duplicate purchases exist with the same combination of main order and backorder information
    __table_args__ = (
        UniqueConstraint('po_number', 'backorder_suffix'),
    )
    
    
    #relationships
    
    purchase_orders = db.relationship(
        "PurchaseOrder",
        back_populates="purchase",
        cascade="all, delete"
    )
    
    department = db.relationship(
        "Department",
        back_populates="purchases"
    )
