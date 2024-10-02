class Locators:
    SITE_NAME = '.name'

class Homepage:

    def __init__(self, browser) -> None:
        self.browser = browser

    def get_page_title(self) -> str:
        return self.browser.select(Locators.SITE_NAME).text
