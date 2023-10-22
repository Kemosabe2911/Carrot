class PersonalLink:
    def __init__(self, user, channel, source, link):
        self.user = user
        self.channel = channel
        self.source = source
        self.link = link

class PersonalDocument:
    def __init__(self, user, channel, source, link):
        self.user = user
        self.channel = channel
        self.source = source
        self.link = link

class PicturesLink:
    def __init__(self, user, channel, title, link, tags):
        self.user = user
        self.channel = channel
        self.title = title
        self.link = link
        self.tags = tags

class EventScheduler:
    def __init__(self, name, desc, type, completed_at, reminded_at, created_at, updated_at, deleted_at, is_completed, is_reminded) :
        self.name = name
        self.desc = desc
        self.type = type
        self.completed_at = completed_at
        self.reminded_at = reminded_at
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        self.is_completed = is_completed
        self.is_reminded = is_reminded

