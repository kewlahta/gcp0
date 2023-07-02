import flask
import os
import json

def test(request: flask.request):
    return str(request)

# this function is the primary entry http entry point for the cloud function
# note: this only serves as a scaffolding template. the auth mechanism used is basic and shouldn't be used in a production environment
def func_entry(request: flask.request) -> json:
    # check the payload for the key
    suppliedKey = None
    
    if "API_KEY" in request.args:
        suppliedKey = request.args.get("API_KEY")
    elif request.is_json and "API_KEY" in request.json:
        suppliedKey = request.json["API_KEY"]

    if suppliedKey == None or (suppliedKey != None and is_valid_auth_key(suppliedKey) == False):
        return "", 401 # unauthorized request
    
    # request meets the basic api key auth requirements so continue processing
    returnMessage = {
        "messsage": "Success"
    }
    return json.dumps(returnMessage), 200


#helper functions
def is_valid_auth_key(tgtKey: str) -> bool:
    retVal = False #explicitly set to false, assume no validation

    acceptableAPIKeyList = os.environ["API_KEY"]

    if tgtKey in acceptableAPIKeyList:
        retVal = True

    return retVal

