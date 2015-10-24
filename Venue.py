# Ýlker Yaðmur - 040090574


# Venue class using in some place definition for tournaments
class Venue:

    def __init__(self, id, name, capacity, location, description):
        self.ID = id
        self.Name = name
        self.Capacity = capacity
        self.Location = location
        self.Description = description

    # A Uniqe id for venue
    def getID(self):
        return self.ID

    def getName(self):
        return self.Name

    def getCapacity(self):
        return self.Capacity

    # Location of Venue it also contains Latitude, Longitude
    def getLocation(self):
        return self.Location

    def getDescription(self):
        return self.Description







