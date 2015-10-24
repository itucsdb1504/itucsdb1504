#isin kirbas 040090600

class Advertise:

    def __init__(self, id, image_url, ext_url, size):
        self.ID = id
        self.ImageUrl = image_url
        self.ExtUrl = ext_url
        self.Size = size

    def getID(self):
        return self.ID

    def getImageUrl(self):
        return self.ImageUrl

    def getExtUrl(self):
        return self.ExtUrl

    def getSize(self):
        return self.Size
