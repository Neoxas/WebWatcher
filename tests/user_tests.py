from webwatcher.user import User
import nose.tools as nose

def test_user():
    andy = User("Andy", "a@b", ["Tests"], 30)
    nose.assert_equal(andy.name, "Andy")
    nose.assert_equal(andy.email, "a@b")
    nose.assert_equal(andy.keywords[0], "Tests")
    nose.assert_equal(andy.budget, 30)


