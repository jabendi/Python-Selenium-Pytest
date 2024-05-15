import time
import pytest
from pages.collected_home_page import HomePage


@pytest.mark.usefixtures()
class TestInstagram:
    def test_get_instagram_url(self):
        instagram = HomePage(self.driver)
        instagram.get_instagram_url()
        time.sleep(10)
        assert "Instagram" in self.driver.title





