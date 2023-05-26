import firebase_admin
from firebase_admin import credentials, auth, messaging

def subscribeToTopic(registrationToken:str, topic:str):
    return messaging.subscribe_to_topic([registrationToken], topic)

def unsubscribeFromTopic(registrationToken:str, topic:str):
    return messaging.unsubscribe_from_topic([registrationToken], topic)