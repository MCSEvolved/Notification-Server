from app import app
from flask import Flask, jsonify, request, Blueprint
from services.NotificationService import topics
from services.RegistrationService import *
from services.AuthService import *

registration_api = Blueprint('registration_api', __name__, template_folder='controllers')

@app.route('/register-device', methods=['POST'])
def registerToken():
    return "Endpoint has been deprecated, use Firebase SDK to subscribe instead", 404
    requestJson = request.get_json()
    try:
        subscribedTopics = requestJson["topics"]
        registrationToken = requestJson["registrationToken"]
    except:
        return "JSON Body Invalid", 400
    token = request.headers.get("Authorization")
    authorized, error = validateTokenForRegistration(token)
    if authorized is False:
        return error, 401
    
    for topic in topics:
        if topic in subscribedTopics:
            subscribeToTopic(registrationToken, topic)
        else:
            unsubscribeFromTopic(registrationToken, topic)
    return "Successfully Registered and Subscribed", 200
