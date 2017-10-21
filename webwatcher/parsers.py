from bs4 import BeautifulSoup as BSoup4

class ParserError(Exception):
    """ Base Parser Exception """
    pass

class InvalidParser(ParserError):
    """ Exception raised for invalid parsers """
    def __init__(self, message):
        self.message = message


class Parser(object):
    NAME = "Parser"
    def __init__(self):
        raise InvalidParser("Can't create Parser objects")

    @property
    def keywords(self):
        if hasattr(self, "_keywords"):
            return self._keywords
        else:
            return "None"

    @keywords.setter
    def keywords(self, keywords):
        self._keywords = keywords

class EbayParser(Parser):
    pass

class GumtreeParser(Parser):
    pass
