from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")

    def is_loaded(self) -> bool:
        self.wait_for(EC.visibility_of_element_located(self.INVENTORY_CONTAINER))
        item = self.driver.find_element(*self.INVENTORY_ITEM)
        return len(items) > 0

    def get_item_names(self):
        items = self.driver.find_elements(*self.INVENTORY_ITEM)
        return [i.find_element(By.CLASS_NAME, "inventory_item_name").text for i in items]