from pages.homepage import Homepage

class Navigator:
    """
    Navigator acts as a test_base.py class where individual instances of class objects are instantiated.

    Note: This is a basic implementation. If we start encountering memory issues we may wish to refactor this to be
        smarter about which objects we need and which we dont for a given test. Not necessary out the gate.
    """

    def __init__(self, browser):
        self.browser = browser
        self.homepage = Homepage(self.browser)
        