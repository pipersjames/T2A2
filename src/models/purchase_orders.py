from main import db 
from models import Purchase, Item

#junction table of purchases and items

purchase_orders = db.Table("purchase_orders",
                           db.Column("purchase_id", db.Integer, db.ForeignKey("purchases.id"), primary_key=True),
                           db.Column("item_id", db.Integer, db.ForeignKey("items.id"), primary_key=True),
                           db.Column("order_date", db.Date),
                           db.Column("received_date", db.Date, nullable=True),
                           db.Column("qty", db.Integer)
                           )

    
    