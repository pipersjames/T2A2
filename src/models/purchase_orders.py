from main import db 

class PurchaseOrder(db.Model):
    __tablename__ = "purchase_orders"
    
    id = db.Column(db.Integer, primary_key=True)
    
    purchase_id = db.Column(db.Integer, db.ForeignKey("purchases.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=False)
    request_id = db.Column(db.Integer, db.ForeignKey("requests.id"), nullable=True)
    order_date = db.Column(db.Date)
    received_date = db.Column(db.Date, nullable=True)
    qty = db.Column(db.Integer)
    
    item = db.relationship(
        "Item",
        back_populates="purchase_orders"
    )

    purchase = db.relationship(
        "Purchase",
        back_populates="purchase_orders"
    )
    
    
    
    request = db.relationship(
        "Request",
        back_populates="purchase_orders"
    )

    
    