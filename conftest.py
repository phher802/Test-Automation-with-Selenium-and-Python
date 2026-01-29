import pytest 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(scope="session")
def base_url():
    #demo app for UI tests
    return "https://www.saucedemo.com"

@pytest.fixture(scope="session")
def api_base_url():
    #demo API for API tests
    return "https://reqres.in/api"

@pytest.fixture(scope="session")
def driver():
    options = ChromeOptions()
    options.add_argument("--headless=new") #remove to see browser
    options.add_argument("--window-size=1280, 800")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver
    driver.quit()