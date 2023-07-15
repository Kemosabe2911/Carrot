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

message_counts = {}

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
        if user in message_counts:
            message_counts[user] += 1
        else:
            message_counts[user] = 1
        client.chat_postMessage(channel=channel, text=text)

@app.route('/message-count', methods=['POST'])
def message_count():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')
    message_count = message_counts.get(user_id, 0)
    client.chat_postMessage(channel=channel_id, text=f"Message: {message_count}")
    
    return Response(), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
