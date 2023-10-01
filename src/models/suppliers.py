from main import db

class Supplier(db.Model):
    __tablename__ = "suppliers"
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(60), unique=True, nullable=False)
    contact_email = db.Column(db.String(60), nullable=False)
    claim_policy = db.Column(db.Integer, nullable=False)
    lead_time = db.Column(db.Integer, nullable=False)
    
    items = db.relationship(
        "Item", 
        back_populates="supplier",
        cascade="all, delete"
        )