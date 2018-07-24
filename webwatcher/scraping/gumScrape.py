# !python3
# gumScrape.py - testing script for parsing the gumtree webpage
from collections import namedtuple
import requests
import bs4
import sys

# Named tuple declaration for each item detail we want
Item = namedtuple( 'Item', ['name', 'price', 'link', 'description', 'location'] )

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

# Parses an item page to extract all content
def ParseItemPageTags( soupTags, hyperlink ):
    titleTags = GetSubSoupTags( soupTags, '[itemprop="name"]' )
    title = titleTags[ 0  ].getText()

    priceTags = GetSubSoupTags( soupTags, '[itemprop="price"]' )
    price = priceTags[ 0 ].getText()

    descriptionTags = GetSubSoupTags( soupTags, '[itemprop="description"]' )
    description = descriptionTags[ 0 ].getText()

    locationTags = GetSubSoupTags( soupTags, '[itemprop="address"]' )
    location = locationTags[ 0 ].getText()

    return Item( name=title, price=price, link=hyperlink, description=description, location=location)

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
    res = GetWebPage( gumTreeBase + link )
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
    gumTreeRequest = gumTreeSearchAddr + 'q=' + search
    print ("Sending request :" + gumTreeRequest )
    res = GetWebPage( gumTreeRequest )
    print("Soupifying...")
    gumSoup = bs4.BeautifulSoup( res.text, "html.parser" )

    hyperlinks = GetIndividualHyperlinks( gumSoup )
    itemList = ScrapeAllItemPages( hyperlinks )

    for item in itemList:
        print ( item )

if __name__ == '__main__':
    main()
