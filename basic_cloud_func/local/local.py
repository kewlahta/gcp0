from flask import Flask, request
import os
import json
import src.main as main

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def basic_func():
    return main.func_entry(request)

# Debugging route to see attributes of the request
@app.route("/debug", methods=["GET", "POST"])
def debug():
    returnDict = {}
    returnDict["request"] = {
        "obj": str(request),
        "method": str(request.method),
        "content": request.json if request.is_json else ""
    }
    returnDict["env_vars"] = str(os.environ)

    return json.dumps(returnDict)

if __name__ == "__main__":
    app.run(debug=True, port=os.environ.get("LOCAL_PORT", "5000"), host="0.0.0.0")