from pytest import mark
from pages.home import *
from pages.dropdown import *


class TestDropdown:

    @mark.regression
    @mark.ui
    def test_chose_items(self, chrome_browser, main_url):

        chrome_browser.get(main_url)
        main_page = Home(chrome_browser)
        main_page.click_on_dropdown()

        dropdown_page = Dropdown(chrome_browser)
        dropdown_page.chose_item("Option 1")
        dropdown_page.chose_item("Option 2")
