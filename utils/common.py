def FetchChannelName(client, channel_id):
    channel_info = client.conversations_info(channel=channel_id)
    channel_name = channel_info["channel"]["name"]
    return channel_name