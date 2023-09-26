from main import db

class RequestType(db.Model):
    __tablename__ = "request_types"
    
    id = db.Column(db.Integer, primary_key=True)
    
    description = db.Column(db.Text(length=20))