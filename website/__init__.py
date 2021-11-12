from flask import Flask
'This create our website folder into a pacakge and whenever it is imported everything in this file is executed automatically'

def create_app():
    #This line initiates a light flask server
    app=Flask(__name__)
    #This line is used to encrypt/decreypt session cookies of our web server. This should be confedential in our prod environment
    app.config['SECRET_KEY']='encrypt'
    #import blueprint for app to use them 
    from .views import views
    from .auth import auth

    #register a blue print with our flask appliation which will can now connected from the browser after routing
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')


    return app