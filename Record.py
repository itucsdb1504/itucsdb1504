# Uğur Büyükyılmaz | 040090560

# Records of players that will be presented to the user

class Record:

    def __init__(self, id, description, player_id, video_id, date):
        self.ID = id
        self.Description = description
        self.PlayerID = player_id
        self.VideoID = video_id
        self.Date = date

    def getID(self):
        return self.ID

    def getDescription(self):
        return self.Description

    def getPlayerID(self):
        return self.PlayerID

    def getVideoID(self):
        return self.VideoID

    def getYear(self):
        return self.Date