from main import db 

#junction table of purchases and items

# purchase_orders = db.Table("purchase_orders",
#                            db.Column("purchase_id", db.Integer, db.ForeignKey("purchases.id"), primary_key=True),
#                            db.Column("item_id", db.Integer, db.ForeignKey("items.id"), primary_key=True),
#                            db.Column("order_date", db.Date),
#                            db.Column("received_date", db.Date, nullable=True),
#                            db.Column("qty", db.Integer)
#                            )


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

    
    