'''This class is responsible for the news to be shown on the site.'''

class News:

    def __init__(self, id, title, content, image_url):
        self.ID = id
        self.Title = title
        self.Content = content
        self.ImageUrl = image_url

    def getID(self):
        return self.ID

    def getTitle(self):
        return self.Title

    def getContent(self):
        return self.Content

    def getImageUrl(self):
        return self.ImageUrl