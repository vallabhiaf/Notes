from flask import Flask
'This create our website folder into a pacakge and whenever it is imported everything in this file is executed automatically'

def create_app():
    #This line initiates a light flask server
    app=Flask(__name__)
    #This line is used to encrypt/decreypt session cookies of our web server. This should be confedential in our prod environment
    app.config['SECRET_KEY']='encrypt'

    return app