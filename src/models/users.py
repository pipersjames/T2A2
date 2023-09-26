from main import db

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    
    first_name = db.Column(db.Text(length=20))
    second_name = db.Column(db.Text(length=100))
    email = db.Column(db.email, unique=True)
    phone_number = db.Column(db.Integer, nullable=True)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable=True)
    
    department = db.relationship(
        "Department",
        back_populates="users"
    )
                              
                              