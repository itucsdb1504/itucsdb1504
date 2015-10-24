# Anýl Yýldýrým - 150130141

# This class is responsible for sponsoring brands.
class Sponsor:

    def __init__(self, id, name, image_url, ext_url):
        self.ID = id
        self.Name = name
        self.ImageUrl = image_url
        self.ExtUrl = ext_url

    def getID(self):
        return self.ID

    def getName(self):
        return self.Name

    def getImageUrl(self):
        return self.ImageUrl

    def getExtUrl(self):
        return self.ExtUrl