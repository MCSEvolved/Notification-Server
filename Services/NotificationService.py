import firebase_admin
from firebase_admin import credentials, auth, messaging

from Models.NotificationModel import Notification

topics = [
    "topic/mc-server",
    "topic/user/weekly-report",
    "topic/power-management/shortage",
    "topic/power-management/reactor-shut-off",
    "topic/service-status/tracker",
    "topic/service-status/storage",
    "topic/service-status/emerald-exchange",
    "topic/service-status/reactor-manager",
    "topic/tracker/error",
    "topic/tracker/warning",
    "topic/tracker/out-of-fuel"
]

def sendNotificationToTopic(topic:str, notification:Notification):
    if topicExists(topic) is False:
        return False
    message = messaging.Message(
        notification={
            'title':notification.title,
            'body':notification.body
        },
        topic=topic
    )

    response = messaging.send(message)
    return response

def topicExists(topic:str):
    if topic in topics:
        return True
    else:
        return False
