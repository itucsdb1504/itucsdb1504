# Uğur Büyükyılmaz | 040090560

# This class is responsible for the videos on the site

class Video:

    def __init__(self, id, title, ext_url, source_type):
        self.ID = id
        self.Title = title
        self.ExtUrl = ext_url
        self.SourceType = source_type

    def getID(self):
        return self.ID

    def getTitle(self):
        return self.Title

    def getExtUrl(self):
        return self.ExtUrl

    def getSourceType(self):
        return self.SourceType