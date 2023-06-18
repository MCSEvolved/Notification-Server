import firebase_admin
from firebase_admin import credentials, auth, messaging
from models.Topics import topicExists

def subscribeToTopic(registrationToken:str, topic:str):
    if topicExists(topic) is False:
        return False
    else:
        response = messaging.subscribe_to_topic([registrationToken], topic)
        return response

def unsubscribeFromTopic(registrationToken:str, topic:str):
    if topicExists(topic) is False:
        return False
    else:
        response = messaging.unsubscribe_from_topic([registrationToken], topic)
        return response