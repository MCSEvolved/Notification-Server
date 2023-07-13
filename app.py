from flask import Flask
import firebase_admin
from firebase_admin import credentials, auth, messaging
from flask import jsonify, request, Blueprint







# def getApp():
#     app = Flask(__name__)
#     from controllers.RegistrationController import registration_api
#     from controllers.NotificationController import notification_api
#     app.register_blueprint(registration_api)
#     app.register_blueprint(notification_api)
#     return app

app = Flask(__name__)


cred = credentials.Certificate("/firebase-cert/certificate.json")
firebase_admin.initialize_app(cred)

from controllers.RegistrationController import registration_api
from controllers.NotificationController import notification_api
app.register_blueprint(registration_api)
app.register_blueprint(notification_api)
#app.run(port=8000, debug=False)





# if __name__ == '__main__':
#     cred = credentials.Certificate("firebase-adminsdk-token.json")
#     firebase_admin.initialize_app(cred)
#     print("RUN")
#     app.run(port=8000, debug=False)

#from controllers import NotificationController
#from controllers import RegistrationController