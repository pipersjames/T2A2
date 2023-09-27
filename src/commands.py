from flask import Blueprint
 
from main import db, bycrypt
from models import Department, Item, Purchase, RequestType, Request, Status, Supplier, User
 
db_commands = Blueprint("db", __name__)
 
@db_commands.cli.command("create")
def create_db():
     db.create_all()
     print("Tables created")
     
@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")
    
@db_commands.cli.command("seed")
def seed_db():
    
    department1 = Department(
        name = "purchasing",
        location = "george st, montgumry",
        open_hours = "3-5pm",
        warehouse_number = None,
    )
    
    db.session.add(department1)
    db.session.commit()
    
    
    user1 = User(
        first_name = "Steve",
        second_name = "Colbert",
        email = "StevieMcAwesome@email.com",
        password = bycrypt.generate_password_hash("password").decode("utf-8"),
        phone_number = "0433345921",
        department_id = 1,
    )
    
    db.session.add(user1)
    db.session.commit()
    
    print("seeding complete")
     
     