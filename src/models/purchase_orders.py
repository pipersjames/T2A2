from main import db 
from models import Purchase, Item
#junction table of purchases and items - not recommended by flask website...

purchase_orders = db.Table("purchase_orders",
                           db.Column("purchase_id", db.Integer, db.ForeignKey("purchases.id"), primary_key=True),
                           db.Column("item_id", db.Integer, db.ForeignKey("items.id"), primary_key=True),
                           db.Column("order_date", db.Date),
                           db.Column("received_date", db.Date, nullable=True),
                           db.Column("qty", db.Integer)
                           )


# class PurchaseOrder(db.Model):
#     __tablename__ = "purchase_orders"
    
#     id = db.Column(db.Integer, primary_key=True)
    
#     purchase_id = db.Column(db.Integer, db.ForeignKey("purchases.id"))
#     item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
#     order_date = db.Column(db.Date)
#     received_date = db.Column(db.Date, nullable=True)
#     qty = db.Column(db.Integer)
    
#     # relationships
    
#     purchase = db.relationship(
#         "Purchase",
#         backref="purchase_orders"
#     )
    
#     item = db.relationship(
#         "Item", 
#         backref="purchase_orders"
#     )
    
#     requests = db.relationship(
#     "Request", 
#     back_populates="purchase_order"
#     )
    
    