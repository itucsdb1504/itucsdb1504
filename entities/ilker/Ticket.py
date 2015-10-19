# Ticket class is using in external tickets definition for matches
class Ticket:

    def __init__(self, id, title, content, price, ext_url):
        self.ID = id
        self.Title = title
        self.Content = content
        self.Price = price
        self.ExtUrl = ext_url

    def getID(self):
        return self.ID

    def getTitle(self):
        return self.Title

    def getContent(self):
        return self.Content

    def getPrice(self):
        return self.Price

    # External Url to sales page of ticket
    def getExtUrl(self):
        return self.ExtUrl
