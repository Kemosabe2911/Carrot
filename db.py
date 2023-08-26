from mongoengine import *
from dotenv import load_dotenv
from pathlib import Path
import os

from models import PersonalLink

# set env path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# connect to db
connect(host=os.environ['DB_URI'])

class PersonalLinks(Document):
    user = StringField(required=True)
    channel = StringField(required=True)
    source = StringField(required=True)
    link = StringField(required=True)


def InsertPersonalLinks(user, channel, source, link):
    personalLink = PersonalLinks(
        user=user,
        channel=channel,
        source=source,
        link=link
    )
    personalLink.save()

def FetchPersonalLinks(user, channel):
    personalLinksArray = []
    for personalLink in PersonalLinks.objects(user=user, channel=channel):
        data = PersonalLink(
            personalLink.user, 
            personalLink.channel, 
            personalLink.source, 
            personalLink.link
        )
        personalLinksArray.append(data)

    return personalLinksArray if len(personalLinksArray) > 0 else None


def UpdatePersonalLinks(user, channel, source ,link):
    PersonalLinks.objects(user=user, channel=channel, source=source).update(link=link)

def DeletePersonalLinks(user, channel, source):
    PersonalLinks.objects(user=user, channel=channel, source=source).delete()