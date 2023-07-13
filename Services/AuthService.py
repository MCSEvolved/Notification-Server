import firebase_admin
from firebase_admin import credentials, auth, messaging

def validateTokenForNotification(token:str):
    #return True, ""
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
        if 'role' in decoded_token and decoded_token['role'] == "isService":
            return True, ""
            
        else:
            print("Claim didnt work")
            return False, "Don't have enough permissions"


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
        if 'role' in decoded_token and decoded_token['role'] == "isPlayer":
            return True, ""
            
        else:
            print("Claim didnt work")
            return False, "Don't have enough permissions"


