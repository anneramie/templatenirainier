from . import db


class User(db.Model):
     __tablename__ = 'User'

     uid = db.Column(db.Integer, primary_key = True)
     email = db.Column(db.String(125), nullable = False)
     username = db.Column(db.String(125), nullable = False)
     password = db.Column(db.String(125), nullable = False)

     def to_json(self):
          return{
               'uid': self.uid,
               'email': self.email,
               'username': self.username,
        
          }

     def __init__(self, username, password, email):
          self.username = username
          self.email = email
          self.password = password