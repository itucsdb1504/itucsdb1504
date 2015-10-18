import uuid


class GeneralUtils:

    def __init__(self):
        print("General Utils")

    def generateID(self):
        return uuid.uuid4()