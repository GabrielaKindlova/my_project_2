from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import path

db = SQLAlchemy ()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ljlknalsk'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'
    db.init_app(app)

    # from .views import views
    from .client_section import client_section
  

    app.register_blueprint(client_section, url_prefix='/')     
    # app.register_blueprint(views, url_prefix='/')
    

    from .models import Clients
    
  
    with app.app_context():
        db.create_all()
        
     
    return app

def create_database(app):
    if not path.exists('website/'+ DB_NAME):
        db.create_all(app=app)
        print('Created database')





