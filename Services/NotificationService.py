import firebase_admin
from firebase_admin import credentials, auth, messaging

from Models.NotificationModel import Notification

def sendNotificationToTopic(topic:str, notification:Notification):
    message = messaging.Message(
        notification={
            'title':notification.title,
            'body':notification.body
        },
        topic=topic
    )

    response = messaging.send(message)
    return response