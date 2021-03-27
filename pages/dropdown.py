from base.page import *


class Dropdown(BasePage):

    def chose_item(self, item):
        BasePage.select_element(self, Locator.drop_down, item)
