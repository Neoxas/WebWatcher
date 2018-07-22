# !python3
# gumScrape.py - testing script for parsing the gumtree webpage
from collections import namedtuple
import requests
import bs4
import sys

# Named tuple declaration for each item detail we want
Item = namedtuple( 'Item', ['name', 'price', 'link'] )

gumTreeBase = 'https://www.gumtree.com'
gumTreeSearchAddr = gumTreeBase + '/search?'
eachAdvertCriteria = '.listing-link'

# Searchs the provided soup tags for a subset of tags
def GetSubSoupTags( soupTags, tagToFind ):
    subSoup = bs4.BeautifulSoup( str( soupTags  ), "html.parser" )
    return subSoup.select( tagToFind )

# Parses each content item to the item named tuple
def ParseSearchPageForLinks( soupTags ):
    hyperlink = soupTags.get( 'href' )

    titleTags = GetSubSoupTags( soupTags, ".listing-title" )
    title = titleTags[ 0 ].getText()

    priceTags = GetSubSoupTags( soupTags, '[itemprop="price"]' )
    price = priceTags[ 0  ][ 'content' ]

    return Item( name=title, price=price, link=hyperlink )

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
    pass

# Scapes all item pages provided and concatinates
def ScrapeAllItemPages( links ):
    pass

# Sends a simple request to the webpage and checks if the status code returns correctly
def GetWebPage( address ):
    res = requests.get( address )
    print("Checking status coide...")
    res.raise_for_status()
    return res

def main():
    search = sys.argv[1]

    print( "Searching for " + search )
    gumTreeRequest = gumTreeSearchAddr + 'q=' + search
    print ("Sending request :" + gumTreeRequest )
    res = GetWebPage( gumTreeRequest )
    print("Soupifying...")
    gumSoup = bs4.BeautifulSoup( res.text, "html.parser" )

    print( "Getting listings with links..." )
    foundItems = gumSoup.select( eachAdvertCriteria )

    print( "Condensing to structures..." )
    itemList = []
    for item in foundItems:
        if( item.get( 'href'  ) is not '' ):
            itemList.append( ParseSearchPageForLinks( item ) )

    print( "Number of structures : " + str( len( itemList ) ) )

if __name__ == '__main__':
    main()
