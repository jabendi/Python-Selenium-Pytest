import pytest


@pytest.mark.usefixtures()
class TestOpenBrowser:
    def test_launch_browser(self):
        print(" ")
        assert "https://www.collectedmagazine.com/" == self.driver.current_url
