from base.page import *


class AddRemoveElements(BasePage):

    def click_add(self, click_time=1):
        if not isinstance(click_time, int):
            raise TypeError(f'click_time type is "{type(click_time)}", expected to be "int"')

        if click_time > 0:
            for _ in range(click_time):
                BasePage.click_on_element_with_text(self, text="Add Element")
        else:
            raise ValueError(f'click_time value is "{click_time}", expected to be above "0"')

    def click_remove(self, click_time=1):
        for _ in range(click_time):
            BasePage.click_on_element_with_text(self, text="Delete")
