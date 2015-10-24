# Uğur Büyükyılmaz | 040090560

# This class is responsible for the videos on the site

class Video:

    def __init__(self, id, title, ext_url, size):
        self.ID = id
        self.Title = title
        self.ExtUrl = ext_url
        self.Size = size

    def getID(self):
        return self.ID

    def getTitle(self):
        return self.Title

    def getExtUrl(self):
        return self.ExtUrl

    def getSize(self):
        return self.Size