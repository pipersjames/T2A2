from main import db 

#junction table of purchases and items

class PurchaseOrder(db.Model):
    __tablename__ = "purchase_orders"
    
    id = db.Column(db.Integer, primary_key=True)
    
    purchase_id = db.Column(db.Integer, db.ForeignKey("purchases.id")),
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    order_date = db.Column(db.Date)
    received_date = db.Column(db.Date, nullable=True)
    qty = db.Column(db.Integer(length=10))
    
    # relationships
    
    purchase = db.relationship(
        "Purchase",
        backref="purchase_orders"
    )
    
    item = db.relationship(
        "Item", 
        backref="purchase_orders"
    )
    
    