import pytest
from selenium.webdriver.common.by import By

from pages.search_page import SearchPage


@pytest.mark.usefixtures()
class TestAddCommentToPhoto:
    def test_leave_comment(self):
        value = "Croatia".upper()  # Assign value to whatever I want to search.
        comment_msg = "Lovely Photos"  # The comment I want to make.

        SearchPage(self.driver).leave_comment(value, comment_msg)
        comments_list = self.driver.find_element(By.CLASS_NAME, "comment-list").text
        assert comment_msg in comments_list



