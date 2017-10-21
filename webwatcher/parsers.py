import requests
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

    def _build_list_of_links(self, page_url):
        response = requests.get(page_url).text
        soup = BSoup4(response, "html.parser")
        list_of_links=[]
        for item in soup.findAll('a', href=True):
            list_of_links.append(item['href'])
        return(list_of_links)

class TestingParser(Parser):
    """ Parser object for testing methods """
    NAME = "Testing Parser"
    def __init__(self):
        pass

class EbayParser(Parser):
    pass

class GumtreeParser(Parser):
    pass
