from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from config import app_config


bycrypt = Bcrypt()
db = SQLAlchemy()
ma = Marshmallow()

def init_app():
    
    load_dotenv()
    
    app =  Flask(__name__)
    
    app.config.from_object("config.app_config")
    
    db.init_app(app)
    
    ma.init_app(app)
    
    return app



    
    

