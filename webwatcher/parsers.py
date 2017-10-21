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

    def __init__(self, keywords):

    @property
    def keywords(self):
        if hasattr(self, "_keywords"):
            return self._keywords
        else:
            return "None"

    @keywords.setter
    def keywords(self, keywords):
        self._keywords = keywords

    def _build_list_of_links(page_url):
        page = requests.get(page_url).text
        soup = BSoup4(page)
        list_of_links=[]
        for item in soup.find_all('a', {'itemprop':'name'}):
            list_of_links.append(item.git('href'))
        return(list_of_links)

    def _get_page_text( self, webpage ):
        return requests.get( webpage )

class EbayParser(Parser):
    pass

class GumtreeParser(Parser):
    def __init__( self, keywords, search_location="England", category="all" ):
        self.keywords = keywords
        self.search_location = search_location
        self.category = category

    @property
    def query( self ):
        # Queries take the format of
        # https://www.gumtree.com/search?category={{category}}&q={{query (spaces are +)}}&search_location={{search location}}
        return( "https://www.gumtree.com/search?category=%s&q=%s&search_location=%s" 
            % (self.category.replace( " ", "+" ),
               self.query.replace( " ", "+" ),
               self.search_location.replace( " ", "+" ) )


