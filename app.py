from flask import Flask
import firebase_admin
from firebase_admin import credentials, auth, messaging

def getApp():
    app = Flask(__name__)
   
    return app

if __name__ == '__main__':
    cred = credentials.Certificate("firebase-adminsdk-token.json")
    firebase_admin.initialize_app(cred)
    app = getApp()
    app.run()



import RegistrationController
import NotificationController
