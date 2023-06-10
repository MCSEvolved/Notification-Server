import firebase_admin
from firebase_admin import credentials, auth, messaging

def validateTokenForNotification(token:str):
    #return True
    try:
        decoded_token = auth.verify_id_token(token)
    except:
        return False
    if decoded_token == None:
        return False
    else:
        if decoded_token['isService'] is False:
            return False
    return True


def validateTokenForRegistration(token:str):
    #return True
    try:
        decoded_token = auth.verify_id_token(token)
    except:
        return False
    if decoded_token == None:
        return False
    else:
        if decoded_token['isPlayer'] is False:
            return False
    return True