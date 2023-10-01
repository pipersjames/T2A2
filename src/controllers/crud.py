from flask import jsonify, request
from main import db
from sqlalchemy.exc import IntegrityError

# returns all records in the given table to the corresponding model input
def get_all_records(model,schema):  
    # try/exception block to handle any unexpected errors using a generic exception response of sqlalchemy.
    try:
        # query all the data in the model
        data = model.query.all()
        # dump the data into a variable loaded in the format of the schema
        result = schema.dump(data)
        # return the data dump in a json format
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching data", "error": str(e)}), 500

# returns a record with an id match from the table of the model selected.
def get_record(model,schema,id):
    # try/exception block to handle any unexpected errors using a generic exception response of sqlalchemy.
    try:
        #get the table name for error handling and feedback
        model_name = model.__tablename__
        #filter the model to return the dict of the id
        query = db.select(model).filter_by(id=id)
        #store the value with the matching id field.
        data = db.session.scalar(query)
        
        #handling for when the id is empty. note by default the primary key is not null so if it does not exist, there is no record.
        if data is None:
            return jsonify({"message": f"Id '{id}' not found in the {model_name} table."}), 404
        #convert using the schema and store in a variable
        result = schema.dump(data)
        #return that variable in a json format for the client
        return jsonify(result), 200
     
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching {model_name} data", "error": str(e)}), 500
    
# deletes a record from the given model as defined by the id.   
def delete_record(model,schema,id):
    # try/exception block to handle any unexpected errors using a generic exception response of sqlalchemy.
    try:
        #get the table name for error handling and feedback
        model_name = model.__tablename__
        #filter the model to return the dict of the id
        q = db.select(model).filter_by(id=id)
        #store the value with the matching id field.
        data = db.session.scalar(q)
        #check to see if a record was found.
        if data is not None:
            #delete the record in the current session
            db.session.delete(data)
            #commit the change to the database
            db.session.commit()
            #confirmation message
            return jsonify(message=f"Record with Id {id} in {model_name} has been deleted successfully!")

        return jsonify(message=f"Id '{id}' in {model_name} was not found. No records deleted")
    
    except Exception as e:
        return jsonify({"message": "An error occurred while fetching {model_name} data", "error": str(e)}), 500
    
# creates a new record in the select model
def create_new_record(model,schema):
    
    # try/exception block to handle any unexpected errors using a generic exception response of sqlalchemy.
    try:
        #load the data provided by the client using the schema
        data_json = schema.load(request.json)
        # create a new instance of the given model using the loaded data
        data = model(**data_json)
        # add the new instance to the session  
        db.session.add(data)
        # commit the change to the current session
        db.session.commit()
        #return the given inputs to the client as confirmation of correct entry.
        return jsonify(schema.dump(data))
    
        # hanlding to roll-back the database session to maintain data integrity
    except IntegrityError as e:
        
        db.session.rollback()
        return jsonify({"message": "Integrity error occurred", "error": str(e)}), 400
    
    except Exception as e:
        # Handle other exceptions
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

# creates a new record in the select model
def create_new_records(model,schema):
    
    # try/exception block to handle any unexpected errors using a generic exception response of sqlalchemy.
    try:
        #load the data provided by the client using the schema
        data_list = schema.load(request.json, many=True)
        # create a new instances of the given model using the loaded data
        new_records = [model(**data) for data in data_list]
        # add the new instances to the session  
        db.session.add_all(new_records)
        # commit the change to the current session
        db.session.commit()
        #returns the new records in json format to the client
        return jsonify(schema.dump(new_records, many=True))
    
    # hanlding to roll-back the database session to maintain data integrity
    except IntegrityError as e:
        
        db.session.rollback()
        return jsonify({"message": "Integrity error occurred", "error": str(e)}), 400
    
    except Exception as e:
        # Handle other exceptions
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


#updates an existing record by id with whatever changes required as long as the field name matches   
def patch_record(model,schema,id):
    
    # try/exception block to handle any unexpected errors using a generic exception response of sqlalchemy.
    
    try:
        #get the table name for error handling and feedback
        model_name = model.__tablename__
        #filter the model to return the dict of the id
        query = db.select(model).filter_by(id=id)
        #store the value with the matching id field.
        data = db.session.scalar(query)
        # check to see if there was a record match and handle the no case.
        if data is None:
            return jsonify(message=f"Cannot update record in {model_name} with id={id}. Not found"), 404
        # load the data provided from the client using the schema
        data_json = schema.load(request.json, partial=True)
        # loop through the different fields and update the different values that correspond
        for field, value in data_json.items():
            setattr(data, field, value)
        #commit the changes to the current session
        db.session.commit()
        #return the changes the client for review
        return jsonify(schema.dump(data))

    except Exception as e:
        return jsonify({"message": "An error occurred while updating {model_name}", "error": str(e)}), 500
    