from genericpath import exists
from flask import Flask
#ORM to talk with sdk for DB 
from flask_sqlalchemy import  SQLAlchemy
from os import path
'This create our website folder into a pacakge and whenever it is imported everything in this file is executed automatically'
#database object created.Everything created will be added to this database object 
db=SQLAlchemy()
#databse name
DB_NAME="database.db"

def create_app():
    #This line initiates a light flask server
    app=Flask(__name__)
    #This line is used to encrypt/decreypt session cookies of our web server. This should be confedential in our prod environment
    app.config['SECRET_KEY']='encrypt'
    #sqllite Databse is stored at the said location 
    app.config['SQLALCHEMY_DATABASE_URI']=f"sqlite:///{DB_NAME}"
    #intialize a db and telling db which app is going to be used with this db 
    db.init_app(app)
    #import blueprint for app to use them 
    from .views import views
    from .auth import auth

    #register a blue print with our flask appliation which will can now connected from the browser after routing
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    #define our classes before we create our DB
    from .models import User,Note

    create_database(app)



    return app

def create_database(app):
    if not path.exists('website/'+ DB_NAME):
        #telling for which app the db is being created 
        db.create_all(app=app)
        print('Created Database !')