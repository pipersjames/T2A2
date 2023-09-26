from main import db

class Department(db.Model):
    __tablename__ = "departments"
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.Text(length=20))
    location = db.Column(db.Text(length=100))
    open_hours = db.Column(db.Text(length=20))
    warehouse_number = db.Column(db.Integer, nullable=True)
    