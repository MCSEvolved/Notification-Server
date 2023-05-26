from __main__ import app
from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, auth, messaging
from Models.NotificationModel import *
from NotificationService import *
from AuthService import *

@app.route('/api/send', methods=['POST'])
def errorNotification():
    token = request.headers.get("Authorization")
    if validateTokenForNotification(token):
        topic:str = request.args.get("topic")
        notificationJson = request.get_json()
        notification = Notification(notificationJson['title'], notificationJson['body'])
        response = sendNotificationToTopic(topic, notification)
        if response is False:
            return "Topic Does Not Exist", 400
        else:
            return response, 200
    else:
        return 'Not Authorized', 401
    