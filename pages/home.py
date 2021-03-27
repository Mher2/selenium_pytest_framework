from base.page import *


class Home(BasePage):

    def click_on_add_remove_elements(self):
        element = BaseElement.get_visible_element(self.driver, Locator.element_with_text % "Add/Remove Elements")
        element.click()

    def click_on_dropdown(self):
        element = BaseElement.get_visible_element(self.driver, Locator.element_with_text % "Dropdown")
        element.click()

    def click_on_javascript_alerts(self):
        element = BaseElement.get_visible_element(self.driver, Locator.element_with_text % "JavaScript Alerts")
        element.click()
