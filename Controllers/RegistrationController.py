from __main__ import app
from flask import Flask, jsonify, request
from NotificationService import topics
from RegistrationService import *
from AuthService import *

@app.route('/api/register-device', methods=['POST'])
def registerToken():
    subscribedTopics = request.get_json()["topics"]
    registrationToken = request.get_json()["registrationToken"]
    token = request.headers.get("Authorization")

    if validateTokenForRegistration(token) is False:
        return "Not Authorized", 401
    
    for topic in topics:
        if topic in subscribedTopics:
            subscribeToTopic(registrationToken, topic)
        else:
            unsubscribeFromTopic(registrationToken, topic)
    return "Successfully Registered and Subscribed to: " + subscribedTopics, 200
