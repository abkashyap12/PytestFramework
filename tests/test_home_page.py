import pytest

class TestHomePage:

    @pytest.mark.smoke
    def test_page_title(self, navigator):
        navigator.browser.visit('https://www.sejda.com/')
        page_title = navigator.homepage.get_page_title()
        assert page_title == 'Sejda'
        