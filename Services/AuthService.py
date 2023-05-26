import firebase_admin
from firebase_admin import credentials, auth, messaging

def validateTokenForNotification(token:str):
    decoded_token = auth.verify_id_token(token)
    if decoded_token == None:
        return False
    else:
        if decoded_token['isService'] is False:
            return False
    return True


def validateTokenForRegistration(token:str):
    decoded_token = auth.verify_id_token(token)
    if decoded_token == None:
        return False
    else:
        if decoded_token['isPlayer'] is False:
            return False
    return True