

class Award:

    def __init__(self, id, description, lastWinnerID):
        self.ID = id
        self.Description = description
        self.LastWinnerID = lastWinnerID

    def getID(self):
        return self.ID

    def getDescription(self):
        return self.Description

    def getLastWinnerID(self):
        return self.PlayerID