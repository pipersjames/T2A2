from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import app_config
import sqlalchemy as sa



bycrypt = Bcrypt()
db = SQLAlchemy()
ma = Marshmallow()

def init_app():
    
    load_dotenv()
    
    app =  Flask(__name__)
    
    app.config.from_object("config.app_config")
    jwt = JWTManager(app)
    
    db.init_app(app)
    
    ma.init_app(app)
    
    from commands import db_commands
    app.register_blueprint(db_commands)
    
    from controllers import registered_controllers
    
    for controller in registered_controllers:
        app.register_blueprint(controller)
        

    
    return app



    
    

