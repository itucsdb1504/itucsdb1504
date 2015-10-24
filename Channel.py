# Ýlker Yaðmur - 040090574

# Channel class is using in match live broadcast linking or showing in app
class Channel:

    def __init__(self, id, name, ext_url):
        self.ID = id
        self.Name = name
        self.ExtUrl = ext_url

    def getID(self):
        return self.ID

    def getName(self):
        return self.Name

    def getExtUrl(self):
        return self.ExtUrl
