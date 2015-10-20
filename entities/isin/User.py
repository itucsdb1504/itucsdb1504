class User:

    def __init__(self, id, firstname, lastname, age, gender, email,account_type):
        self.ID = id
        self.FirstName = firstname
        self.LastName = lastname
        self.Age = age
        self.Gender = gender
        self.Email = email
        self.AccountType = account_type

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

    def getAccountType(self):
        return self.AccountType
