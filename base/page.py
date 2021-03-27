from base.element import *
from resources.locator import *


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_on_element_with_text(self, text):
        element = BaseElement.get_visible_element(self.driver, Locator.element_with_text % text)
        element.click()
        return None

    def read_element_with_text(self, text):
        BaseElement.get_visible_element(self.driver, Locator.element_with_text % text)
        return None

    def get_element_with_text(self, text):
        element = BaseElement.get_visible_element(self.driver, Locator.element_with_text % text)
        return element

    def select_element(self, locator, item):
        element = BaseElement.get_select_element(self.driver, locator)
        element.select_by_visible_text(item)
        return None

    def click_alert_ok(self):
        BaseElement.get_popup_element(self.driver)
        self.driver.switch_to.alert.accept()

    def click_alert_cancel(self):
        BaseElement.get_popup_element(self.driver)
        self.driver.switch_to.alert.dismiss()

    def fill_alert(self, text):
        BaseElement.get_popup_element(self.driver)
        self.driver.switch_to.alert.send_keys(text)
