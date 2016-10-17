import os, sys, json

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['Get'])
def verify():

    if requests.args.get("hub.mode")=='subscribe' and requests.args.get("hub.challenge"):
        if not request.args.get('hub.verify_token')== os.environ['VERIFY_TOKEN']:
            return "Token Mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello! This is ThreadsBot |X|"
