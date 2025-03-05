import eventlet
eventlet.monkey_patch()
from flask import Flask
from .extensions import db, migrate, login_manager, socketio, ip_address, save_data, jwt ,create_access_token, jwt_required, get_jwt_identity 
from .sockets import socketio
from os import path
import os
import pymysql



pymysql.install_as_MySQLdb()


def create_website():

     app = Flask(__name__)
     app.config["SECRET_KEY"] = os.urandom(24)
     app.config["JWT_SECRET_KEY"] = 'aobwduiao'
  

     app.config["SQLALCHEMY_DATABASE_URI"] = (
          f"mysql+pymysql://root:%40%23OctObEr102704@{ip_address}/React1?charset=utf8"
     )
     # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') For deployment






  
     from .api.auth_api import auth
     from .api.user_api import user_api

     app.register_blueprint(auth)
     app.register_blueprint(user_api)

     db.init_app(app)
     jwt.init_app(app)
     migrate.init_app(app, db)
     socketio.init_app(app, async_mode="eventlet", cors_allowed_origins="*")



     create_database(app)

     return app


def create_database(app):

    with app.app_context():
        db.create_all()
        print("Created Database!")
