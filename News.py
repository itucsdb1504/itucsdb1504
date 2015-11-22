# Uğur Büyükyılmaz | 040090560

# This class is responsible for the news to be shown on the site

class News:

    def __init__(self, id, title, content, image_url, date):
        self.ID = id
        self.Title = title
        self.Content = content
        self.ImageUrl = image_url
        self.Date = date

    def getID(self):
        return self.ID

    def getTitle(self):
        return self.Title

    def getContent(self):
        return self.Content

    def getImageUrl(self):
        return self.ImageUrl

    def getDate(self):
        return self.Date