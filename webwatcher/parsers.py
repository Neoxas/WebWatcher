class ParserError(Exception):
    """ Base Parser Exception """
    pass

class InvalidParser(ParserError):
    """ Exception raised for invalid parsers """
    def __init__(self, message):
        self.message = message


class Parser(object):
    def __init__(self):
        raise InvalidParser("Can't create Parser objects")

class EbayParser(Parser):
    pass

class GumtreeParser(Parser):
    pass
