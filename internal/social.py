from db import InsertPersonalLinks, UpdatePersonalLinks, DeletePersonalLinks
from utils.consts import SocialLinkInsertCommand, SocialLinkUpdateCommand, SocialLinkDeleteCommand

def PerformSocialLinkOperation(user, channel, data):
    operation = data[0]
    if operation == SocialLinkInsertCommand:
        InsertPersonalLinks(
            user= user,
            channel= channel,
            source= data[1],
            link= data[2]
        )
    elif operation == SocialLinkUpdateCommand:
        UpdatePersonalLinks(
            user= user,
            channel= channel,
            source= data[1],
            link= data[2]
        )
    elif operation == SocialLinkDeleteCommand:
         DeletePersonalLinks(
            user= user,
            channel= channel,
            source= data[1],
        )