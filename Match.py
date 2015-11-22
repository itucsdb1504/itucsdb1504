# Anıl Yıldırım - 150130141

# This class is responsible for Matches between players.
class Match:

    def __init__(self, id, tournamentID, venueID, player1, player2, isLive, score):
        self.ID = id
        self.TournamentID = tournamentID
        self.VenueID = venueID
        self.Player1 = player1
        self.Player2 = player2
        self.IsLive = isLive
        self.Score = score
        self.TournamentName = " "
        self.VenueName = " "
        self.Player1Name = " "
        self.Player2Name = " "

    def getID(self):
        return self.ID

    def getTournamentID(self):
        return self.TournamentID

    def getTournamentName(self):
        return self.TournamentName

    def getVenueID(self):
        return self.VenueID

    def getVenueName(self):
        return self.VenueName

    def getPlayer1(self):
        return self.Player1

    def getPlayer1Name(self):
        return self.Player1Name

    def getPlayer2(self):
        return self.Player2

    def getPlayer2Name(self):
        return self.Player2Name

    def isLive(self):
        return self.IsLive

    def getScore(self):
        return self.Score