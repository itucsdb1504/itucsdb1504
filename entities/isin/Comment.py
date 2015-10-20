class Comment:

    def __init__(self, id, username, title, content, date):
        self.ID = id
        self.Username = username
        self.Title = title
        self.Content = content
        self.Date = date


    def getID(self):
        return self.ID

    def getUsername(self):
        return self.Username

    def getTitle(self):
        return self.Title

    def getContent(self):
        return self.Content

    def getDate(self):
        return self.Date
