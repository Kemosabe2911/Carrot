from db import InsertPersonalLinks, UpdatePersonalLinks, DeletePersonalLinks
from utils.consts import SlackInsertCommand, SlackUpdateCommand, SlackDeleteCommand

def PerformSocialLinkOperation(user, channel, data):
    operation = data[0]
    if operation == SlackInsertCommand:
        InsertPersonalLinks(
            user= user,
            channel= channel,
            source= data[1],
            link= data[2]
        )
    elif operation == SlackUpdateCommand:
        UpdatePersonalLinks(
            user= user,
            channel= channel,
            source= data[1],
            link= data[2]
        )
    elif operation == SlackDeleteCommand:
         DeletePersonalLinks(
            user= user,
            channel= channel,
            source= data[1],
        )