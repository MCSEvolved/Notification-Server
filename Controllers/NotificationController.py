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
    if validateToken(token):
        topic:str = request.args.get("topic")
        notificationJson = request.get_json()
        notification = Notification(notificationJson['title'], notificationJson['body'])
        return sendNotificationToTopic(topic, notification), 200
    else:
        return 'Not Authorized', 401
    