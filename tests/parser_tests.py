import nose.tools as nose
import webwatcher.parsers as parsers

TEST_LINK = "https://robtom5.github.io/Webpage/testing.html"
@nose.raises(parsers.InvalidParser)
def test_Parser():
    """
    test to check that Parser objects
    cannot be created
    """
    parsers.Parser()

def test_building_list():
    testing = parsers.TestingParser()
    nose.assert_equal(
            testing._build_list_of_links(TEST_LINK),
            [TEST_LINK]
            )
