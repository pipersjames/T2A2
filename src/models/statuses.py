from main import db

class Status(db.Model):
    __tablename__ = "statuses"
    
    id = db.Column(db.Integer, primary_key=True)
    
    description = db.Column(db.String(length=20), unique=True, nullable=False)
    
    requests = db.relationship(
    "Request", 
    back_populates="status",
    cascade="all, delete"
    )
    