import pytest 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(scope="session")
def base_url():
    #demo app for UI tests
    return "https://www.saucedemo.com"

@pytest.fixture(scope="session")
def api_base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="function") #use function instead of session to get a new browser for testing
def driver():
    options = ChromeOptions()
    options.add_argument("--headless=new") #remove to see browser
    options.add_argument("--window-size=1280, 800")

    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()