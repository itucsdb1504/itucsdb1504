# Anıl Yıldırım - 150130141

# This class is responsible for Tournaments information.
class Tournament:

    def __init__(self, id, name, venueID, round, player_count, last_winnerID, awardID):
        self.ID = id
        self.Name = name
        self.VenueID = venueID
        self.Round = round
        self.PlayerCount = player_count
        self.LastWinnerID = last_winnerID
        self.AwardID = awardID
        self.VenueName = " "
        self.LastWinnerName = " "
        self.AwardName = " "

    def getID(self):
        return self.ID

    def getName(self):
        return self.Name

    def getVenueID(self):
        return self.VenueID

    def getVenueName(self):
        return self.VenueName

    def getRound(self):
        return self.Round

    def getPlayerCount(self):
        return self.PlayerCount

    def getLastWinnerID(self):
        return self.LastWinnerID

    def getLastWinnerName(self):
        return self.LastWinnerName

    def getAwardID(self):
        return self.AwardID

    def getAwardName(self):
        return self.AwardName