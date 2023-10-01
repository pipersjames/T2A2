from main import db

class RequestType(db.Model):
    __tablename__ = "request_types"
    
    id = db.Column(db.Integer, primary_key=True)
    
    description = db.Column(db.String(length=20), unique=True,nullable=False)
    
    requests = db.relationship(
    "Request", 
    back_populates="request_type",
    cascade="all, delete"
    )