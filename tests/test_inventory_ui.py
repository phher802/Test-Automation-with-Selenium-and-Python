from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_shows_products_after_login(driver, base_url):
    login_page = LoginPage(driver);
    inventory_page = InventoryPage(driver)

    login_page.open_login(base_url)
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_loaded(), "Inventory page did not load"

    names = inventory_page.get_item_names()
    assert len(names) > 0, "No inventory items found"