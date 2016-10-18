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


@app.route('/', methods=['POST'])
def webhook():

	data = request.get_json()
	log(data) # Maintain log for testing

	if data["object"] == 'page':
		for entry in data['entry']:

			for messaging_event in entry["messaging"]:
				if messaging_event.get('message'):

					sender_id = messaging_event['sender']['id']
					recipient_id = messaging_event['sender']['id']
					message_text = messaging_event['message']['text']

					send_message(sender_id, "cheers, mate")

				if messaging_event.get('delivery'):
					pass

				if messaging_event.get('optin'):
					pass

				if messaging_event:
					pass

	return 'Okie Dokie', 200


def send_message(recipient_id, message_text):
	log('Sent messge to {recipient}: {text}'.format(recipient= recipient_id, text=message_text))

	params = {'access_token' os.environ['PAGE_ACCESS_TOKEN']}

	
	pass