#import db from the current package 
from . import db
#class that helps user login, USermixin is inherit by the user object later 
from flask_login import UserMixin
#current time 
from sqlalchemy.sql import func

class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    
    #foregin key relationship reference an id(primary_key) to different databse 1 to many relationship, one user many notes 
    #sql will represnt User as user
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))



#User Schema blueprint for the user object(will create later) which is inheriting stuff from db object and usermixin object 

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    
    #all the notes(note id) belonging to a particilar user would be stored here as a list(reference of a class`)
    notes=db.relationship('Note')
