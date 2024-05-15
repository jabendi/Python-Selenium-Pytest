import pytest
from pages.collected_home_page import HomePage


@pytest.mark.usefixtures()
class TestAbout:
    def test_about(self):
        about = HomePage(self.driver)
        about.get_about_info()
        assert "ABOUT" in self.driver.title




