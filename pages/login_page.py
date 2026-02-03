from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error-message-container.error h3[data-test='error]")

    def open_login(self, base_url: str):
        self.open(base_url)
        self.wait_for(EC.visibility_of_element_located(self.USERNAME))

    def login(self, username: str, password: str):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)

        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()
    
    def get_error_text(self) -> str:
        try:
        # wait until the error is visible
            el = self.wait_for(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return el.text.strip()
        except TimeoutException:
            return ""
