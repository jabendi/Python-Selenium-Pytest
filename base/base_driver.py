from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_presence_of_element(self, locator_type, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator_type, locator)))
        return element

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element


