from main import db

class Supplier(db.Model):
    __tablename__ = "suppliers"
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.Integer)
    contact_email = db.Column(db.String(60))
    claim_policy = db.Column(db.Integer)
    lead_time = db.Column(db.Integer)