import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter

# set env path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']
# client.chat_postMessage(channel='#test', text="Hello World!")

@app.route("/slack/events", methods=["GET", "POST"])
def handle_slack_events():
    if request.method == "GET":
        challenge = request.args.get("challenge")
        return challenge, 200

    # Handle other events using the POST method
    # data = request.get_json()
    # print(data)
    # if "event" in data:
    #     event = data["event"]
    #     event_type = event.get("type")

    #     if event_type == "message":
    #         channel = event.get("channel")
    #         text = event.get("text")
    #         user = event.get("user")

    #         if BOT_ID != user:
    #             # Add your logic to handle the message event
    #             # For example, you can print the message details
    #             print(f"Received message: '{text}' in channel: {channel} from user: {user}")
    #             client.chat_postMessage(channel=channel, text=text)
    
    return "", 200

@slack_event_adapter.on('message')
def message(payload):
    event= payload.get('event', {})
    channel = event.get('channel')
    user = event.get('user')
    text = event.get('text')

    if BOT_ID != user:
        # Add your logic to handle the message event
        # For example, you can print the message details
        print(f"Received message: '{text}' in channel: {channel} from user: {user}")
        client.chat_postMessage(channel=channel, text=text)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
