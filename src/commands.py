from flask import Blueprint
 
from main import db, bycrypt
from models import Department, Item, purchase_orders, Purchase, RequestType, Request, Status, Supplier, User
from datetime import datetime
from flask import current_app

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
    
    #base tables
    status1 = Status(       #required seed items
        description = "new"
    )
    
    status2 = Status(
        description = "in progress"
    )
    
    status3 = Status(
        description = "completed"
    )
    
    request1 = RequestType(
        description = "incorrect supply"
    )
    
    request2 = RequestType(
        description = "over supply"
    )
    
    request3 = RequestType(
        description = "short supply"
    )
    
    request4 = RequestType(
        description = "cancellation"
    )
    
    request5 = RequestType(
        description = "ETA update"
    )
    
    
    department1 = Department(            #test seed items
        name = "purchasing",
        location = "george st, montgumry",
        open_hours = "3-5pm",
        warehouse_number = None,
    )
    
    department2 = Department(
        name = "sales",
        location = "george st, montgumry",
        open_hours = "3-5pm",
        warehouse_number = None,
    )
    
    department3 = Department(
        name = "Salisbury",
        location = "52, Salisbury st",
        open_hours = "3-5pm",
        warehouse_number = 42,
    )
    
    supplier1 = Supplier(
        name = "Kmart",
        contact_email = "kmart@email.com",
        claim_policy = 14,
        lead_time = 7,
    )
    
    supplier2 = Supplier(
        name = "OutsideStore",
        contact_email = "fishingisgreat@email.com",
        claim_policy = 30,
        lead_time = 14,
    )
    
    db.session.add_all([
        status1,
        status2,
        status3,
        request1,
        request2,
        request3,
        request4,
        request5,
        supplier1,
        supplier2,
        department1,
        department2,
        department3,])
    db.session.commit()
    
    #dependant tables
    user1 = User(                #default admin user for creation
        first_name = "buyer",
        second_name = "Colbert",
        email = "buyer@email.com",
        password = bycrypt.generate_password_hash("password").decode("utf-8"),
        phone_number = "0433345921",
        department_id = 1,
        admin = True,
    )
    
    user2 = User(
        first_name = "seller",
        second_name = "Colbert",
        email = "seller@email.com",
        password = bycrypt.generate_password_hash("password2").decode("utf-8"),
        phone_number = "0433345921",
        department_id = 2,
    )
    
    user3 = User(
        first_name = "warehouse teamember",
        second_name = "Frank",
        email = "warehouse@email.com",
        password = bycrypt.generate_password_hash("password1").decode("utf-8"),
        phone_number = "0433345921",
        department_id = 3,
    )
    
    purchase1 = Purchase(
        po_number = 443,
        backorder_suffix = None,
        department_id = 3,
        supplier_id = 1,
    )
    
    purchase2 = Purchase(
        po_number = 444,
        backorder_suffix = None,
        department_id = 3,
        supplier_id = 2,
    )
    
    purchase3 = Purchase(
        po_number = 444,
        backorder_suffix = "AA",
        department_id = 3,
        supplier_id = 2,
    )
    
    item1 = Item(
        internal_code = "A5643",
        supp_code = "read-46",
        description = "book of love",
        supp_id = 1,
    )
    
    item2 = Item(
        internal_code = "A4433",
        supp_code = "read-43",
        description = "book of cheese",
        supp_id = 1,
    )
    
    item3 = Item(
        internal_code = "B3332",
        supp_code = "SH3KM",
        description = "Dark sunglasses",
        supp_id = 2,
    )
    
    item4 = Item(
        internal_code = "B5973",
        supp_code = "SH5KS",
        description = "Reading glasses",
        supp_id = 2,
    )
    
    item5 = Item(
        internal_code = "B3321",
        supp_code = "KJCREAM",
        description = "sun tan lotion",
        supp_id = 2,
    )
    
    item6 = Item(
        internal_code = "B8493",
        supp_code = "KJBACK",
        description = "sun shirt",
        supp_id = 2,
    )
    
    
    
    db.session.add_all([
        user1, 
        user2, 
        user3,
        purchase1,
        purchase2,
        purchase3,
        item1,
        item2,
        item3,
        item4,
        item5,
        item6,])
    db.session.commit()
    
    #junction table direct data insert
    purchase = Purchase.query.filter_by(po_number=443).first()
    item = Item.query.filter_by(internal_code="A5643").first()

    purchase1 = {
        'purchase_id': purchase.id,
        'item_id': item.id,
        'order_date': datetime(2023, 9, 21),
        'received_date': datetime(2023, 9, 28),
        'qty': 10
    }

    db.session.execute(purchase_orders.insert().values(**purchase1))
    db.session.commit()
    
    
    request1 = Request(
        purchase_order_id = 1,
        item_id = 1,
        request_type_id = 1,
        status_id = 1,
        user_id = 3,
        comment = "sent book about eating pandas instead",
        issue_qty = 1,
        docket_number = "inv-4532",
        created_at = datetime.now(),
        completion_comment = None,
    )
    
    db.session.add(request1)
    db.session.commit()
    
    print("seeding complete")
     
     