import firebase_admin
from firebase_admin import credentials, auth, messaging

def sendNotificationToTopic(topic:str, title:str, body:str):
    message = messaging.Message(
        notification={
            'title':title,
            'body':body
        },
        topic=topic
    )

    response = messaging.send(message)
    return response