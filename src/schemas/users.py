from main import ma
from marshmallow import fields
from schemas.departments import department_schema

class UserSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = (
            "id", 
            "first_name", 
            "second_name", 
            "email", 
            "password", 
            "phone_number",
            "department_id", 
            "department",
        )

        load_only = ["id","department_id","password"]
    
    email = fields.Email(
        required=True,
        )
    
    department = fields.Nested(department_schema, exclude=("id",))
    
    

user_schema = UserSchema()
users_schema = UserSchema(many=True)