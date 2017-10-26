#import requests
#from bs4 import BeautifulSoup as BSoup4
import pickle

from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError


import parsers

class EbayParser(parsers.Parser):
    def __init__(self, User="", keywords="", MinPrice=0, MaxPrice=1000):
        self.User = User
        self.keywords = keywords
        self.MinPrice = MinPrice
        self.MaxPrice = MaxPrice
        self.Responses = {}

    def run_search(self):
        try:
            api = Finding(config_file='./etc/ebay.yaml',siteid='EBAY-GB')
            response = api.execute('findItemsAdvanced',
                    {
                        'keywords': self.keywords,
                        'itemFilter': self.ItemFilter,
                        'sortOrder': 'BestMatch'
                        }
                    )
            for item in response.dict()['searchResult']['item']:
                self.Responses[str(item['itemId'])] = {
                        'title'  : item['title'],
                        'price'  : item['sellingStatus']['convertedCurrentPrice'],
                        'viewurl': item['viewItemURL'],
                        }

        except ConnectionError as e:
            print("Error")
            print(e)
            print(e.response.dict())

    def _log_searches(self):
        pass

    def _save_searches(self):
        with open(self.User+ self.keywords + '.pkl', 'wb') as file:
            pickle.dump(self.Responses, file, pickle.HIGHEST_PROTOCOL)

    def _load_searches(self):
        with open(self.User + self.keywords + '.pkl', 'rb') as file:
            return pickle.load(file)

    @property
    def MinPrice(self):
        return str(self._MinPrice)

    @MinPrice.setter
    def MinPrice(self, value):
        self._MinPrice = value

    @property
    def MaxPrice(self):
        return str(self._MaxPrice)

    @MaxPrice.setter
    def MaxPrice(self, value):
        self._MaxPrice = value

    @property
    def ItemFilter(self):
        return [
            {'name': 'MinPrice', 'value': self.MinPrice,
                'paramName': 'Currency', 'paramValue': 'GBP'},
            {'name': 'MaxPrice', 'value': self.MaxPrice,
                'paramName': 'Currency', 'paramValue': 'GBP'}
        ]



test_ebay=EbayParser(User = "Me", keywords=["Python","Book"])
test_ebay.run_search()
