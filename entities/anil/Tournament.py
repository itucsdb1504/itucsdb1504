class Tournament:

    def __init__(self, id, name, venue, round, player_count, last_winner, award):
        self.ID = id
        self.Name = name
        self.Venue = venue
        self.Round = round
        self.PlayerCount = player_count
        self.LastWinner = last_winner
        self.Award = award

    def getID(self):
        return self.ID

    def getName(self):
        return self.Name

    def getVenue(self):
        return self.Venue

    def getRound(self):
        return self.Round

    def getPlayerCount(self):
        return self.PlayerCount

    def getLastWinner(self):
        return self.LastWinner

    def getAward(self):
        return self.Award