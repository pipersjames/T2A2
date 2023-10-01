from main import ma

class RequestTypeSchema(ma.Schema):
    class Meta:
        fields = "id", "description"

        load_only = ["id",]

request_type_schema = RequestTypeSchema()
request_types_schema = RequestTypeSchema(many=True)