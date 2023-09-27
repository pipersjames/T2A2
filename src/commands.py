from flask import Blueprint
 
from main import db, bycrypt
from models import Department, Item, PurchaseOrder, Purchase, RequestType, Request, Status, Supplier, User
 
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
    pass
     
     