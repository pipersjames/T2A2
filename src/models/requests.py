from main import db
from sqlalchemy import DateTime
from sqlalchemy.sql import func
# from sqlalchemy import ForeignKeyConstraint

class Request(db.Model):
    __tablename__ = "requests"
    
    id = db.Column(db.Integer, primary_key=True)
    
    purchase_order_id = db.Column(db.Integer, nullable=False)
    #item_id = db.Column(db.Integer, nullable=False)
    request_type_id = db.Column(db.Integer, db.ForeignKey("request_types.id"))
    status_id = db.Column(db.Integer, db.ForeignKey("statuses.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.Column(db.String(length=100), nullable=True)
    issue_qty = db.Column(db.Integer)
    docket_number = db.Column(db.String(length=30), nullable=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    completion_comment = db.Column(db.String(length=100), default = None, nullable=True)
    
    # table relationships
    request_type = db.relationship(
        "RequestType", 
        back_populates="requests"
        )
    status = db.relationship(
        "Status",
        back_populates="requests"
        )
    user = db.relationship(
        "User",
        back_populates="requests"
        )
    purchase_orders = db.relationship(
        "PurchaseOrder",
        primaryjoin="Request.id == PurchaseOrder.request_id",
        back_populates="request"
    )
    
    # purchase_orders = db.relationship(
    #     "Purchase",
    #     secondary="purchase_orders",  # Name of the junction table
    #     primaryjoin="and_(Request.id == purchase_orders.c.request_id, "
    #                 "Request.purchase_order_id == purchase_orders.c.purchase_id, "
    #                 "Request.item_id == purchase_orders.c.item_id)",
    #     secondaryjoin="and_(Purchase.id == purchase_orders.c.purchase_id, "
    #                   "Item.id == purchase_orders.c.item_id)",
    #     back_populates="requests",
    # )

    # items = db.relationship(
    #     "Item",
    #     secondary="purchase_orders",  # Name of the junction table
    #     primaryjoin="and_(Request.id == purchase_orders.c.request_id, "
    #                 "Request.purchase_order_id == purchase_orders.c.purchase_id, "
    #                 "Request.item_id == purchase_orders.c.item_id)",
    #     secondaryjoin="and_(Item.id == purchase_orders.c.item_id, "
    #                   "Purchase.id == purchase_orders.c.purchase_id)",
    #     back_populates="requests",
    # )
    
    #foreign key constraint for the purchase_orders table connecting the relationship of the 
    
    # __table_args__ = (
    #     db.ForeignKeyConstraint(
    #         ['purchase_order_id', 'item_id'],
    #         ['purchase_orders.purchase_id', 'purchase_orders.item_id']
    #         ),
    #     )
    