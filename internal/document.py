from db import InsertPersonalDocuments, UpdatePersonalDocuments, DeletePersonalDocuments
from utils.consts import SlackInsertCommand, SlackUpdateCommand, SlackDeleteCommand

def PerformDocumentsOperation(user, channel, data):
    operation = data[0]
    if operation == SlackInsertCommand:
        InsertPersonalDocuments(
            user= user,
            channel= channel,
            source= data[1],
            link= data[2]
        )
    elif operation == SlackUpdateCommand:
        UpdatePersonalDocuments(
            user= user,
            channel= channel,
            source= data[1],
            link= data[2]
        )
    elif operation == SlackDeleteCommand:
         DeletePersonalDocuments(
            user= user,
            channel= channel,
            source= data[1],
        )