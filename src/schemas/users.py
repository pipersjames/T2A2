from main import ma
from marshmallow import fields

class UserSchema(ma.Schema):
    class Meta:
        email = fields.Email(
        required=True,
        )
        
        fields = "id", "first_name", "second_name", "email", "phone_number", "department_id"


user_schema = UserSchema()
users_schema = UserSchema(many=True)