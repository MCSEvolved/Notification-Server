import firebase_admin
from firebase_admin import credentials, auth, messaging

def validateTokenForNotification(token:str):
    #return True
    try:
        decoded_token = auth.verify_id_token(token)
    except:
        print("Couldn't verify token")
        return False, "Token is Invalid"
    if decoded_token == None:
        print("Could Not decode token")
        return False, "Could Not Decode Token"
    else:
        print(decoded_token)
        if 'isService' in decoded_token and decoded_token['isService'] is True:
            return True, ""
            
        else:
            print("Claim didnt work")
            return False, "Not Authorized"


def validateTokenForRegistration(token:str):
    #return True
    try:
        decoded_token = auth.verify_id_token(token)
    except:
        print("Couldn't verify token")
        return False, "Token is Invalid"
    if decoded_token == None:
        print("Couldn't decode token")
        return False, "Could Not Decode Token"
    else:
        print(decoded_token)
        if 'isPlayer' in decoded_token and decoded_token['isPlayer'] is True:
            return True, ""
            
        else:
            print("Claim didnt work")
            return False, "Not Authorized"


