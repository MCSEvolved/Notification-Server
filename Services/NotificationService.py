import firebase_admin
from firebase_admin import credentials, auth, messaging

from models.NotificationModel import NotificationModel
from models.Topics import topicExists


def sendNotificationToTopic(topic:str, notification:NotificationModel):
    if topicExists(topic) is False:
        return False
    message = messaging.Message(
        notification=messaging.Notification(
            title=notification.title,
            body=notification.body,
        ),
        topic=topic,
        apns=messaging.APNSConfig(
            payload=messaging.APNSPayload(
                aps=messaging.Aps(
                    sound='default',
                    badge=1
                )
            )
        )
    )

    response = messaging.send(message)
    return response


