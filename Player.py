class Player:
    def __init__(self, id, firstname, lastname, age, gender, email, nationality, turned_pro, location, nickname=None, money_list_erarnings, birthday):
        self.ID = id
        self.FirstName = firstname
        self.LastName = lastname
        self.Age = age
        self.Gender = gender
        self.Email = email
        self.Nationality = nationality
        self.TurnedPro = turned_pro
        self.Location = location
        self.Nickname = nickname
        self.MoneyListEarnings = money_list_erarnings
        self.Birthday = birthday

    def getID(self):
        return self.ID

    def getFirstName(self):
        return self.FirstName

    def getLastName(self):
        return self.LastName

    def getAge(self):
        return self.Age

    def getGender(self):
        return self.Gender

    def getEmail(self):
        return self.Email

    def getNationality(self):
        return self.Nationality

    def getTurnedPro(self):
        return self.TurnedPro

    def getLocation(self):
        return self.Location

    def getNickname(self):
        return self.Nickname

    def getMoneyListEarnings(self):
        return self.MoneyListEarnings

    def getBirthday(self):
        return self.Birthday