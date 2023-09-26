from main import db

class Supplier(db.Model):
    __tablename__ = "suppliers"
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.Integer)
    contact_email = db.Column(db.email)
    claim_policy = db.Column(db.Integer(length=2))
    lead_time = db.Column(db.Integer(length=2))