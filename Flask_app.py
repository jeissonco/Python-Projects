from flask import Flask

def create_app():
    app = Flask(__name__)

    #this is going to encrypt and secure the data, thats the secret key of the app
    app.config['SECRET_KEY'] ='tortuga.15'

    return app
