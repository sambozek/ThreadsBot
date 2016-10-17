import os, sys, json

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['Get'])
def verify():
    """ test to verify that the heroku app is functional. Return errors """
    if request.args.get("hub.mode")=='subscribe' and request.args.get("hub.challenge"):
        if not request.args.get('hub.verify_token')== os.environ['VERIFY_TOKEN']:
            return "Token Mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello! This is ThreadsBot |X|"
