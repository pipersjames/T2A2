from main import db

class Department(db.Model):
    __tablename__ = "departments"
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(length=20), unique=True)
    location = db.Column(db.String(length=100))
    open_hours = db.Column(db.String(length=20))
    warehouse_number = db.Column(db.Integer, nullable=True)
   
   # relationships
    users = db.relationship(
        "User",
        back_populates="department"
    ) 
    
    