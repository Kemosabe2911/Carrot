from db import InsertPicturesLink, UpdatePicturesLink, DeletePicturesLink
from utils.consts import SlackInsertCommand, SlackUpdateCommand, SlackDeleteCommand

def PerformDocumentsOperation(user, channel, data):
    operation = data[0]
    if operation == SlackInsertCommand:
        tagsList = data[3].split(',')
        if len(tagsList) < 1 :
            tagsList = []
        InsertPicturesLink(
            user= user,
            channel= channel,
            title= data[1],
            link= data[2],
            tags= tagsList
        )
    elif operation == SlackUpdateCommand:
        UpdatePicturesLink(
            user= user,
            channel= channel,
            source= data[1],
            link= data[2]
        )
    elif operation == SlackDeleteCommand:
         DeletePicturesLink(
            user= user,
            channel= channel,
            source= data[1],
        )