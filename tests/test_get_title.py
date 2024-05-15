import pytest


@pytest.mark.usefixtures()
class TestTitle:
    def test_get_title(self):
        print(" ")
        print(self.driver.title)
        assert "COLLECTED" in self.driver.title
