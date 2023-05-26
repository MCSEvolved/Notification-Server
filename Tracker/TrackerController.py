from __main__ import app
from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, auth, messaging
from NotificationService import *
from AuthService import *

@app.route('/api/tracker/error', methods=['POST'])
def errorNotification():
    token = request.headers.get("Authorization")
    if validateToken(token):
        topic:str = "topic/tracker/error"
        return sendNotificationToTopic(topic, "Error", "Turtle x has error: ArrayOutOfIndexException: 69"), 200
    else:
        return 'Not Authorized', 401
    

@app.route('/api/tracker/warning', methods=['POST'])
def warningNotification():
    token = request.headers.get("Authorization")
    if validateToken(token):
        topic:str = "topic/tracker/warning"
        return sendNotificationToTopic(topic, "Warning", "Turtle x has warning: Out of building blocks"), 200
    else:
        return 'Not Authorized', 401

@app.route('/api/tracker/out-of-fuel', methods=['POST'])
def outOfFuelNotification():
    token = request.headers.get("Authorization")
    if validateToken(token):
        topic:str = "topic/tracker/out-of-fuel"
        return sendNotificationToTopic(topic, "Out of Fuel", "Turtle x has run out of fuel"), 200
    else:
        return 'Not Authorized', 401