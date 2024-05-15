import pytest
from pages.search_page import SearchPage


# from ddt import ddt, data, file_data, unpack

@pytest.mark.usefixtures()
class TestSearchSomething:
    def test_search_something(self):
        value = "Firenze".upper()  # Assign value to whatever I want to search.
        SearchPage(self.driver).search_something(value)
        assert value in self.driver.title
