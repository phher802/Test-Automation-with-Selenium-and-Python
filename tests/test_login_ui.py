from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_successful_login(driver, base_url):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_login(base_url)
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_loaded(), "Inventory page did not load after login"

def test_invalid_login_shows_error(driver, base_url):
    login_page = LoginPage(driver)

    login_page.open_login(base_url)
    login_page.login("standard_user", "wrong_password")

    error_text = login_page.get_error_text()
    assert "Username and password do not match" in error_text or "Epic sadface" in error_text
    