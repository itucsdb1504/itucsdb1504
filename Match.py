# Anýl Yýldýrým - 150130141

# This class is responsible for Matches between players.
class Match:

    def __init__(self, id, tournament, player1, player2, isLive, score):
        self.ID = id
        self.Tournament = tournament
        self.Player1 = player1
        self.Player2 = player2
        self.IsLive = isLive
        self.Score = score

    def getID(self):
        return self.ID

    def getTournament(self):
        return self.Tournament

    def getPlayer1(self):
        return self.Player1

    def getPlayer2(self):
        return self.Player2

    def isLive(self):
        return self.IsLive

    def getScore(self):
        return self.Score