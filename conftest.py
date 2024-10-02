import logging
import pytest
from utils.webdriver import get_driver
from utils.browser import Browser
from utils.navigator import Navigator



def pytest_addoption(parser):
    parser.addini("browser", help="Browser to be used for testing. Chrome by default")
    parser.addoption("--browser", action="store", default='chrome')
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s",
                        datefmt="%m-%d-%Y %H:%M:%S")


@pytest.fixture(scope="function")
def get_browser(request):
    return request.config.getoption("--browser") if request.config.getoption("--browser") else request.config.getini("browser")


@pytest.fixture(scope="function")
def driver(get_browser):
    driver = get_driver(get_browser)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def navigator(driver):
     browser = Browser(driver)
     return Navigator(browser)
