from main import db
from sqlalchemy import DateTime
from sqlalchemy.sql import func

class Request(db.Model):
    __tablename__ = "requests"
    
    id = db.Column(db.Integer, primary_key=True)
    
    purchase_order_id = db.Column(db.Integer, db.ForeignKey("purchase_orders.id"), nullable=False)
    request_type_id = db.Column(db.Integer, db.ForeignKey("request_types.id"),nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey("statuses.id"),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"),nullable=False)
    comment = db.Column(db.String(length=100), nullable=True)
    issue_qty = db.Column(db.Integer, nullable=False)
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
    purchase_order = db.relationship(
        "PurchaseOrder",
        back_populates="requests"
    )
    