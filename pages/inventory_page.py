from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    def is_loaded(self) -> bool:
        #returns true when the inventory page is visible and has at leasat one item
        try:
            self.wait_for(EC.visibility_of_element_located(self.TITLE))
            items = self.wait_for(EC.presence_of_all_elements_located(self.INVENTORY_ITEMS))

            return len(items) > 0
        except TimeoutException:
            return False


    def get_item_names(self):
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return [i.find_element(By.CLASS_NAME, "inventory_item_name").text for i in items]