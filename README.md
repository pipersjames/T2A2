## Supplier Request form API


R1

When a company grows to a certain extent processes are often compartmentalized to gain efficiences. It is also done to regulate certain actions and ensure that are handled appropriately. This API is designed to take requests from different departments of a business and feed them to the purchasing division to liase/make adjustments accordingly. A similiar comparision would be an email ticketing system. By design the components of the request are rigid enough to streamline workflow to select team members but with enough variability that situations can be explained. Emails and phone numbers of users are in the system so that if the feedback is insuffiecent they can be contacted. 

R2

Team members handle different suppliers as workload increases and each issues can often take quite a bit of back and forth as well as a good understanding of supplier-client relations. On the other hand some tasks are a simple tick and flick. This API intends to solve this issue by allowing the purchasing officer to get the specific data they need related to the workflow they are handling. 

R3

I've chosen the relational database model for 2 reasons. Because this is what we have learnt how to handle and it provides a solid amount of data validation to ensure that data entry is correct going into the model. It has good security...

R4

R5

R6

![API ERD](./resources/API%20ERD.png)

Tables


Requests
- request_id int NOT NULL (PK)
- junction_id int NOT NULL (FK)
- request_type_id int NOT NULL (FK)
- status_id int  NOT NULL (FK)
- comments varchar(100) NULLABLE
- request_qty int NULLABLE
- user_id int  NOT NULL (FK)
- docket_number varchar(30) NULLABLE
- completion_comment varchar(100), NULLABLE
- Date timestamp default: current_timestamp NOT NULL

Request Types
- request_type_id int NOT NUll (PK)
- Description varchar(20) NULLABLE

Status'
-status_id int NOT NULL (PK)
- description varchar(20) NULLABLE

Users
- user_id int NOT NULL (PK)
- first_name varchar(20) NOT NULL
- second_name varchar(20) NOT NULL
- email email NOT NULL
- phone varchar(20) NOT NULL
- department_id int  NOT NULL (FK)

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

Purchase orders
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
- supplier_id id NOT NULL (FK)

Junction Table - PO's and Items
- junction_id int NOT NULL (PK)
- PO_id int NOT NULL (FK)
- item_id int NOT NULL (FK)
- order_date date NOT NULL
- ETA_date date (default: order_date + 7 days) NOT NULL
- item_qty int NOT NULL


R7

R8

R9



