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