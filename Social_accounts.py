class Social_accounts:

    def __init__(self, id, twitterLink, instagramLink, facebookLink):
        self.ID = id
        self.TwitterLink = twitterLink
        self.InstagramLink = instagramLink
        self.FacebookLink = facebookLink

    def getID(self):
        return self.ID

    def getTwitterLink(self):
        return self.TwitterLink

    def getInstagramLink(self):
        return self.InstagramLink

    def getFacebookLink(self):
        return self.FacebookLink