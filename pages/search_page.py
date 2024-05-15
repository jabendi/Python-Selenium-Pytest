from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from utilities.utils import Utils


class SearchPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    Search_button = "Header-search-form-submit"
    Search_box = "/html/body/div[4]/div[2]/div/main/section/div/div/div[1]/form/input"
    Search_results = "search-result"
    List_of_Comments = "comment-list"
    Comment_button = "comment-btn"
    Name_of_commenter = "u-field-input"
    Confirm_comment = "G7iNL9mHtAig74Ar4KM2"

    def search_something(self, value):
        self.driver.find_element(By.CLASS_NAME, self.Search_button).click()
        self.driver.find_element(By.XPATH, self.Search_box).send_keys(value)
        self.driver.implicitly_wait(10)
        self.driver.find_elements(By.CLASS_NAME, "search-result")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-result"))).click()
        self.log.info("Search successful")

    def leave_comment(self, value, comment_msg):
        self.driver.find_element(By.CLASS_NAME, self.Search_button).click()
        self.driver.find_element(By.XPATH, self.Search_box).send_keys(value)
        self.driver.implicitly_wait(10)
        self.driver.find_elements(By.CLASS_NAME, "search-result")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-result"))).click()
        self.driver.find_element(By.NAME, "comment").send_keys(comment_msg)
        self.driver.find_element(By.CLASS_NAME, self.Comment_button).click()
        self.driver.find_element(By.CLASS_NAME, self.Name_of_commenter).send_keys("Jaime")
        self.driver.find_element(By.CLASS_NAME, self.Confirm_comment).click()
        self.log.info("Comment has been left successfully")

