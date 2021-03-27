from pytest import mark
from pages.home import *
from pages.add_remove_elements import *


class TestAddRemoveElements:

    @mark.regression
    @mark.ui
    def test_add_element(self, chrome_browser, main_url):

        chrome_browser.get(main_url)
        main_page = Home(chrome_browser)
        main_page.click_on_add_remove_elements()

        add_remove_page = AddRemoveElements(chrome_browser)
        add_remove_page.click_add()

    @mark.regression
    @mark.ui
    def test_remove_element(self, chrome_browser, main_url):

        chrome_browser.get(main_url)
        main_page = Home(chrome_browser)
        main_page.click_on_add_remove_elements()

        add_remove_page = AddRemoveElements(chrome_browser)
        add_remove_page.click_add()
        add_remove_page.click_remove()
