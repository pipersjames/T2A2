from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import app_config
import sqlalchemy as sa



bcrypt = Bcrypt()
db = SQLAlchemy()
ma = Marshmallow()

def init_app():
    
    load_dotenv()
    
    app =  Flask(__name__)
    
    app.config.from_object("config.app_config")
    app.json.sort_keys = False
    
    jwt = JWTManager(app)
    
    db.init_app(app)
    
    ma.init_app(app)
    
    from commands import db_commands
    app.register_blueprint(db_commands)
    
    from controllers import registered_controllers
    
    for controller in registered_controllers:
        app.register_blueprint(controller)
        
    db_engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db_inspector = sa.inspect(db_engine)

    if not db_inspector.has_table("users"):
        with app.app_context():
            db.drop_all()
            db.create_all()
            app.logger.info("New database initialized!")
    else:
        app.logger.info("Database already exists!")
        

    
    return app



    
    

