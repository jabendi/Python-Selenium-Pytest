import pytest
from pages.collected_home_page import HomePage


@pytest.mark.usefixtures()
class TestHeader:

    def test_header_click_refreshes_page(self):
        header_attribute = HomePage(self.driver)
        header_attribute.header_click_refreshes_page()
        assert "new_title != initial_title"








