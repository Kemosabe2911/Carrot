
import os

def GetSlackToken():
    return os.environ['SLACK_TOKEN']

def GetSlackSigningSecret():
    return os.environ['SIGNING_SECRET']

def GetDatabaseURI():
    return os.environ['DB_URI']