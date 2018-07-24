# !python3
# gumScrape.py - testing script for parsing the gumtree webpage
from collections import namedtuple
import requests
import bs4
import sys

# Named tuple declaration for each item detail we want
Item = namedtuple( 'Item', ['name', 'price', 'link', 'description', 'location'] )

ebayBase = 'https://www.ebay.co.uk'
ebaySearchAddr = ebayBase + '/sch/i.html?_nkw='
eachAdvertCriteria = '.vip'

# Searchs the provided soup tags for a subset of tags
def GetSubSoupTags( soupTags, tagToFind ):
    subSoup = bs4.BeautifulSoup( str( soupTags  ), "html.parser" )
    return subSoup.select( tagToFind )

# Parses an item page to extract all content
def ParseItemPageTags( soupTags, hyperlink ):
    titleTags = GetSubSoupTags( soupTags, '[itemprop="name"]' )
    title = titleTags[ 0  ].getText()

    priceTags = GetSubSoupTags( soupTags, '[itemprop="price"]' )
    price = priceTags[ 0 ][ 'content' ]

    return Item( name=title, price=price, link=hyperlink, description='', location='' )

# Gets the hyperlinks to each item from a top level gum tree page
def GetIndividualHyperlinks( pageSoup ):
    print( "Finding hyperlinks..." )
    foundItems = pageSoup.select( eachAdvertCriteria )
    hyperlinks = []
    for item in foundItems:
        href = item.get( 'href' )

        # gumtree inserts some weird content items. bad ones have no hyperlink
        if( href is not '' ):
            hyperlinks.append( href )

    print( "Found " + str( len( hyperlinks  ) ) + " hyperlinks!" )
    return hyperlinks

# Scrapes the provided item page
def ScrapeItemPage( link ):
    res = GetWebPage( link )
    itemPageSoup = bs4.BeautifulSoup( res.text, "html.parser" )
    return ParseItemPageTags( itemPageSoup, link )

# Scapes all item pages provided and concatinates
# Returns : list containing all item objects from each web page
def ScrapeAllItemPages( links ):
    itemList = []
    for link in links:
        itemList.append( ScrapeItemPage( link ) )
    return itemList

# Sends a simple request to the webpage and checks if the status code returns correctly
def GetWebPage( address ):
    res = requests.get( address )
    print("Checking status code...")
    res.raise_for_status()
    return res

def main():
    search = sys.argv[1]

    print( "Searching for " + search )
    ebayRequest = ebaySearchAddr + search
    print ("Sending request :" + ebayRequest )
    res = GetWebPage( ebayRequest )
    print("Soupifying...")
    ebaySoup = bs4.BeautifulSoup( res.text, "html.parser" )

    hyperlinks = GetIndividualHyperlinks( ebaySoup )
    itemList = ScrapeAllItemPages( hyperlinks )

    for item in itemList:
        print ( item )

if __name__ == '__main__':
    main()
