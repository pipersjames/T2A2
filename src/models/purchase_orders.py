from main import db 
from sqlalchemy import UniqueConstraint 

class PurchaseOrder(db.Model):
    __tablename__ = "purchase_orders"
    
    id = db.Column(db.Integer, primary_key=True)
    
    purchase_id = db.Column(db.Integer, db.ForeignKey("purchases.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=False)
    order_date = db.Column(db.Date,nullable=False)
    received_date = db.Column(db.Date, nullable=True)
    qty = db.Column(db.Integer, nullable=False)
    
    __table_args__ = (
        UniqueConstraint('purchase_id', 'item_id'),
    )
    
    item = db.relationship(
        "Item",
        back_populates="purchase_orders"
    )

    purchase = db.relationship(
        "Purchase",
        back_populates="purchase_orders"
    )
    
    requests = db.relationship(
        "Request",
        back_populates="purchase_order",
        cascade="all, delete"
    )

    
    