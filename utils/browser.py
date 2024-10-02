from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser:

    def __init__(self, driver):
        self._driver = driver
        self.timeout_length = 5

    def visit(self, url):
        """ Convenience function for navigating to a specified url
        :param url: String that is the URL
        """
        self._driver.get(url)

    def select(self, selector: str, wait_for_elem_to_be_visible=True, _timeout_length=10):
        """ Function used for selecting and returning a single WebElement matching the CSS Selector provided
        :param selector: The CSS Selector for the element on a page you wish to get the WebElement for.
        :param wait_for_elem_to_be_visible: Boolean to determine if test waits for element to be visible. True by default
        :param _timeout_length: int value that represents the number of seconds to wait for an element.
        """
        timeout = _timeout_length if _timeout_length is not None else self.timeout_length
        try:
            if wait_for_elem_to_be_visible:
                self.wait_for_element_to_display(selector, _timeout_length=timeout)
            element = self._driver.find_element(By.CSS_SELECTOR, selector)
        except TimeoutException:
            raise NoSuchElementException()
        return element
    
    def wait_for_element_to_display(self, selector, _timeout_length=None, step=0.05):
        """ Function that will wait for an element to be displayed on a given page.
         :param selector: The CSS Selector for the element on a page you wish to get the WebElement for.
         :param _timeout_length: int value that represents the number of seconds to wait for an element.
         :param step: interval by which selenium polls the DOM.
         """
        timeout = _timeout_length if _timeout_length is not None else self.timeout_length
        try:
            return WebDriverWait(self._driver, timeout, step, (NoSuchElementException, StaleElementReferenceException)). \
                until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        except TimeoutException:
            raise NoSuchElementException(selector)
        