import pytest
from pages.collected_home_page import HomePage


@pytest.mark.usefixtures()
class TestFacebook:
    def test_get_facebook_url(self):
        HomePage(self.driver).get_facebook_url()
        assert "Facebook" in self.driver.title

