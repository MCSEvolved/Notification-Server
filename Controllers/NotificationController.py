from app import app
from flask import Flask, jsonify, request, Blueprint
import firebase_admin
from firebase_admin import credentials, auth, messaging
from models.NotificationModel import *
from services.NotificationService import *
from services.AuthService import *


notification_api = Blueprint('notification_api', __name__, template_folder='controllers')

@app.route('/notifications/send', methods=['POST'])
def sendNotification():
    token = request.headers.get("Authorization")
    authorized, error = validateTokenForNotification(token)
    if authorized:
        try:
            topic:str = request.args.get("topic")
        except:
            return "Missing Argument: topic", 400
        
        notificationJson = request.get_json()
        try:
            notification = NotificationModel(notificationJson['title'], notificationJson['body'])
        except:
            return "JSON Body Invalid", 400
        
        response = sendNotificationToTopic(topic, notification)
        if response is False:
            return "Topic Does Not Exist", 400
        else:
            return "Successfully Send Notifications to " + topic, 200
    else:
        return error, 401
    