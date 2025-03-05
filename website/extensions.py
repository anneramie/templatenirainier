from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt

db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO()
login_manager = LoginManager()
jwt = JWTManager()

ip_address = "192.168.1.33"


def save_data(data):

     try:
          db.session.add(data)
          db.session.commit()

          return('success')
     except:
          db.session.rollback()
          return('failed')
