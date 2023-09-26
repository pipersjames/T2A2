from main import ma
from marshmallow import fields

class UserSchema(ma.Schema):
    class Meta:
        fields = "id", "first_name", "second_name", "email", "phone_number", "department_id"


user_schema = UserSchema()
user_schemas = UserSchema(many=True)