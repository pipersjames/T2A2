from main import db

class User(db.Model):
    __tablename__ = "users"
   
    #primary key 
    id = db.Column(db.Integer, primary_key=True)
    
    # table fields
    first_name = db.Column(db.String(length=20))
    second_name = db.Column(db.String(length=100))
    email = db.Column(db.String(length=60), unique=True)
    password = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(length=10), nullable=True)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable=True)
    admin = db.Column(db.Boolean, default=False)
    
    # relationships
    department = db.relationship(
        "Department",
        back_populates="users"
    )
    
    requests = db.relationship(
    "Request", 
    back_populates="user",
    cascade="all, delete"
    )
                              
                              