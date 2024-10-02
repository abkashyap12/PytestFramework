from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver(get_browser) -> webdriver:
    """Function to create the Selenium Webdriver instance"""
    chrome_options = Options()
    if get_browser == "chrome":
        chrome_options.add_argument("--start-maximized")
    elif get_browser == "chrome-headless":
        chrome_options.add_argument("--headless")
    else:
        print("Driver not supported")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver
    