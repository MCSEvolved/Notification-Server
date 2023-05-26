import firebase_admin
from firebase_admin import credentials, auth, messaging

def validateToken(token:str):
    decoded_token = auth.verify_id_token(token)
    if decoded_token == None:
        return False
    else:
        if decoded_token['isService'] is False:
            return False
    return True