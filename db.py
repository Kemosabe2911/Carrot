from mongoengine import *
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime

from config import GetDatabaseURI

from models import PersonalLink, PersonalDocument, PicturesLink, EventScheduler

# set env path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# connect to db
connect(host=GetDatabaseURI())

class PersonalLinks(Document):
    user = StringField(required=True)
    channel = StringField(required=True)
    source = StringField(required=True)
    link = StringField(required=True)

class PersonalDocuments(Document):
    user = StringField(required=True)
    channel = StringField(required=True)
    source = StringField(required=True)
    link = StringField(required=True)

class PictureLink(DynamicDocument):
    user = StringField(required=True)
    channel = StringField(required=True)
    title = StringField(required=True)
    link = StringField(required=True)

class EventSchedule(Document):
    name = StringField(required=True)
    desc = StringField()
    type = StringField(required=True)
    completed_at = DateTimeField(required=True)
    reminded_at = DateTimeField(required=True)
    created_at = DateTimeField(required=True)
    updated_at = DateTimeField(required=True)
    deleted_at = DateTimeField()
    is_completed = BooleanField()
    is_reminded = BooleanField()
    date = StringField()

### Personal Links
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

### Personal Documents
def InsertPersonalDocuments(user, channel, source, link):
    personalDocument = PersonalDocuments(
        user=user,
        channel=channel,
        source=source,
        link=link
    )
    personalDocument.save()

def FetchPersonalDocuments(user, channel):
    personalDocumentsArray = []
    for personalDoc in PersonalDocuments.objects(user=user, channel=channel):
        data = PersonalDocument(
            personalDoc.user, 
            personalDoc.channel, 
            personalDoc.source, 
            personalDoc.link
        )
        personalDocumentsArray.append(data)

    return personalDocumentsArray if len(personalDocumentsArray) > 0 else None


def UpdatePersonalDocuments(user, channel, source ,link):
    PersonalDocuments.objects(user=user, channel=channel, source=source).update(link=link)

def DeletePersonalDocuments(user, channel, source):
    PersonalDocuments.objects(user=user, channel=channel, source=source).delete()

### My Pictures
def InsertPicturesLink(user, channel, title, link, tags):
    personalLink = PictureLink(
        user=user,
        channel=channel,
        title=title,
        link=link
    )
    personalLink.tags = tags
    personalLink.save()

def FetchPicturesLink(user, channel):
    myPicturesArray = []
    for picturesLink in PictureLink.objects(user=user, channel=channel):
        data = PicturesLink(
            picturesLink.user, 
            picturesLink.channel, 
            picturesLink.title, 
            picturesLink.link,
            picturesLink.tags
        )
        myPicturesArray.append(data)

    return myPicturesArray if len(myPicturesArray) > 0 else None

def FetchPicturesLinkByTags(user, channel, tags):
    myPicturesArray = []
    for picturesLink in PictureLink.objects(user=user, channel=channel, tags=tags):
        data = PicturesLink(
            picturesLink.user, 
            picturesLink.channel, 
            picturesLink.title, 
            picturesLink.link,
            picturesLink.tags
        )
        myPicturesArray.append(data)

    return myPicturesArray if len(myPicturesArray) > 0 else None


def UpdatePicturesLink(user, channel, title ,link):
    PictureLink.objects(user=user, channel=channel, title=title).update(link=link)

def DeletePicturesLink(user, channel, title):
    PictureLink.objects(user=user, channel=channel, title=title).delete()


### Event Schedule
def InsertEventSchedule(name, desc, type, completed_at, reminded_at, date):
    eventSchedule = EventSchedule(
        name = name,
        desc = desc,
        type = type,
        completed_at = completed_at,
        reminded_at = reminded_at,
        created_at = datetime.now(),
        updated_at = datetime.now(),
        is_completed = False,
        is_reminded = False,
        date = date,
    )
    eventSchedule.save()

def FetchScheduleEvents(type):
    scheduleEventArray = []
    for scheduleEvent in EventSchedule.objects(type = type):
        data = EventScheduler(
            scheduleEvent.name,
            scheduleEvent.desc,
            scheduleEvent.type,
            scheduleEvent.completed_at,
            scheduleEvent.reminded_at,
            scheduleEvent.created_at,
            scheduleEvent.updated_at,
            scheduleEvent.deleted_at,
            scheduleEvent.is_completed,
            scheduleEvent.is_reminded,
            scheduleEvent.date,
        )
        scheduleEventArray.append(data)

    return scheduleEventArray if len(scheduleEventArray) > 0 else None

def FetchScheduleEventsByDate(type, date):
    scheduleEventArray = []
    for scheduleEvent in EventSchedule.objects(type = type, date= date):
        data = EventScheduler(
            scheduleEvent.name,
            scheduleEvent.desc,
            scheduleEvent.type,
            scheduleEvent.completed_at,
            scheduleEvent.reminded_at,
            scheduleEvent.created_at,
            scheduleEvent.updated_at,
            scheduleEvent.deleted_at,
            scheduleEvent.is_completed,
            scheduleEvent.is_reminded,
            scheduleEvent.date,
        )
        scheduleEventArray.append(data)

    return scheduleEventArray if len(scheduleEventArray) > 0 else None

def CompleteScheduleEvent(name, type):
    EventScheduler.objects(name=name, type=type).update(is_completed=True, completed_at=datetime.now())