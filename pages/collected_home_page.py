from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class HomePage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    Facebook_link = "//a[normalize-space()='Facebook']"
    Instagram_link = "//a[normalize-space()='Instagram']"
    About_link = "//a[@class='Header-nav-item'][normalize-space()='ABOUT']"
    About_content = "//div[@id='block-dc36dd11d72dfccf5938']//div[@class='sqs-block-content']"
    Header = "//a[@class='Header-branding']"

    def get_facebook_url(self):
        self.driver.find_element(By.XPATH, self.FacebooK_link).click()
        self.driver.implicitly_wait(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.implicitly_wait(3)
        url = self.driver.current_url
        self.log.info(url)

    def get_instagram_url(self):
        self.driver.find_element(By.XPATH, self.Instagram_link).click()
        self.driver.implicitly_wait(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.implicitly_wait(3)
        url = self.driver.current_url
        print(" ")
        self.log.info(url)

    def get_about_info(self):
        self.driver.find_element(By.XPATH, self.About_link).click()
        self.driver.implicitly_wait(3)
        print(" ")
        print(" ")
        self.log.info(self.driver.find_element(By.XPATH, self.About_content).text)

    def header_click_refreshes_page(self):
        initial_title = self.driver.title

        self.driver.find_element(By.XPATH, self.Header).click()
        new_title = self.driver.title
        self.log.info("Page refreshed successfully")
