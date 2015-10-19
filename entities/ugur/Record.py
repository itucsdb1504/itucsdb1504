'''records of players that will be presented to the user...'''

class Record:

    def __init__(self, id, name, player_name, year):
        self.ID = id
        self.Name = name
        self.PlayerName = player_name
        self.Year = year

    def getID(self):
        return self.ID


    def getName(self):
        return self.Name

    def getPlayerName(self):
        return self.PlayerName

    def getYear(self):
        return self.Year