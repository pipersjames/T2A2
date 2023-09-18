import os 

class BaseConfig(object):
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        db = os.environ.get("DATABASE_URI")
        
        if db is None:
            raise ValueError("no DATABASE_URI found")
        
        return db
    
    
class DevelopmentConfig(BaseConfig):
    DEBUG=True
    
class ProductionConfig(BaseConfig):
    pass

class TestConfig(BaseConfig):
    pass

env = os.environ.get("FLASK_ENV")

if env == "development":
    app_config = DevelopmentConfig()
elif env == "test":
    app_config = TestConfig()
else:
    app_config = ProductionConfig()