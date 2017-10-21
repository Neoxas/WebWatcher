import nose.tools as nose
import webwatcher.parsers as parsers

@nose.raises(parsers.InvalidParser)
def test_Parser():
    """
    test to check that Parser objects
    cannot be created
    """
    parsers.Parser()


