## Supplier Request form API


R1

When a company grows to a certain extent processes are often compartmentalized to gain efficiences. It is also done to regulate certain actions and ensure that are handled appropriately. This API is designed to take requests from different departments of a business and feed them to the purchasing division to liase/make adjustments accordingly. A similiar comparision would be an email ticketing system. By design the components of the request are rigid enough to streamline workflow to select team members but with enough variability that situations can be explained. Emails and phone numbers of users are in the system so that if the feedback is insuffiecent they can be contacted. 

R2

Team members handle different suppliers as workload increases and each issues can often take quite a bit of back and forth as well as a good understanding of supplier-client relations. On the other hand some tasks are a simple tick and flick. This API intends to solve this issue by allowing the purchasing officer to get the specific data they need related to the workflow they are handling. 

R3

I've chosen the relational database model for 2 reasons. Because this is what we have learnt how to handle and it provides a solid amount of data validation to ensure that data entry is correct going into the model. It has good security...

R4

R5

Endpoints ;

Auth

register user
login
check-session





Users

 

Get all user information – admin only

Get own user information

Create new user

Update admin – admin only

Update department

Delete user – own record only

Delete user any – admin only

 

Departments

 

Create department – admin only

Get all departments

Get specific department information

Delete department – admin only

Update department values

 

Items

 

Create item – in bulk – admin

Get all items –

Get specific item information – back fill all PO’s related

Delete item

Update information on item

 

Suppliers

 

Create supplier – admin

Get all suppliers

Get specific supplier information

Delete supplier – cascade delete all items

Update supplier information – purchasing/admin only

 

Requests

 

Create request

Get request

Get requests based on specific parameters partularly the request type or status

Update request – access depending on current status

Delete request – access depending on current status

 

Status and request types

 

Create new – admin only

Get all

Delete – admin only

Update description admin only

 

Purchases

 

Create new in bulk – admin only

Get purchase information – pull data from purchase order table

Update PO

Delete PO – cascade delete all entries on the purchase orders table with the same PO – admin only

 

Purchase orders ? don’t know if anything is required as this is attended to through the other two tables.

 

Auth

 

Don’t know.

R6

![API ERD](./resources/API%20ERD.png)

Tables


Requests
- request_id int NOT NULL (PK)
- Purchaseorder_id int NOT NULL (FK)
- request_type_id int NOT NULL (FK)
- status_id int  NOT NULL (FK)
- comments varchar(100) NULLABLE
- request_qty int NULLABLE
- user_id int  NOT NULL (FK)
- docket_number varchar(30) NULLABLE
- completion_comment varchar(100), NULLABLE
- created_at timestamp server_default: current_timestamp NOT NULL

RequestTypes
- request_type_id int NOT NUll (PK)
- Description varchar(20) NOT NULL

Status'
-status_id int NOT NULL (PK)
- description varchar(20) NOT NULL

Users
- user_id int NOT NULL (PK)
- first_name varchar(20) NOT NULL
- second_name varchar(20) NOT NULL
- email email NOT NULL
- phone varchar(20) NOT NULL
- department_id int  NULLABLE (FK)

Departments
- department_id int NOT NULL (PK)
- name varchar(20) NOT NULL
- location varchar(100) NOT NULL
- open_hours varchar(20) NOT NULL
- warehouse_number int NULLABLE

Suppliers
- supplier_id int NOT NULL (PK)
- name varchar(20) NOT NULL
- contact email NOT NULL
- return_policy int NOT NULL
- lead_time int NOT NULL

Purchases
- PO_id int NOT NULL (PK)
- PO_number int NOT NULL
- Backorder_suffix varchar(2) NULLABLE
- warehouse_id int NOT NULL (FK)
- supplier_id int NOT NULL (FK)

Items
- item_id int NOT NULL (PK)
- internal_code varchar(10) NOT NULL
- supplier_code varchar(10) Unique NOT NULL
- description text NULLABLE
- unit_of_measure varchar(10) NOT NULL
- supplier_id id NOT NULL (FK)

PurchaseOrders - PO's and Items
- purchase_order_id int NOT NULL (PK)
- Purchase_id int NOT NULL (FK)
- item_id int NOT NULL (FK)
- order_date date NOT NULL
- received_date date NULLABLE
- item_qty int NOT NULL


R7

R8

R9



