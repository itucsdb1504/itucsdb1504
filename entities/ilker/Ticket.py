# Ticket class is using in external tickets definition for matches

'''root_dir = os.path.abspath(os.path.dirname(__file__))
utils_path = os.path.abspath(root_dir).split(os.sep)[-3]

from utils_path import GeneralUtils'''

class Ticket:

    def __init__(self, id, title, content, price, ext_url):
        self.ID = id
        self.Title = title
        self.Content = content
        self.Price = price
        self.ExtUrl = ext_url

    def getID(self):
        utils = GeneralUtils()

        return utils.generateID()

    def getTitle(self):
        return self.Title

    def getContent(self):
        return self.Content

    def getPrice(self):
        return self.Price

    # External Url to sales page of ticket
    def getExtUrl(self):
        return self.ExtUrl
