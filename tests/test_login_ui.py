from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time

def test_successful_login(driver, base_url):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_login(base_url)
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_loaded(), f"Inventory page did not load, URL was: {driver.current_url}"

def test_invalid_login_shows_error(driver, base_url):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver) 

    login_page.open_login(base_url)
    login_page.login("standard_user", "wrong_password")

    time.sleep(1)
    
    assert not inventory_page.is_loaded(), "Should not land on inventory page with wrong password"
    