from base.page import *


class JSAlerts(BasePage):

    def click_on_js_alert(self):
        BasePage.click_on_element_with_text(self, text="Click for JS Alert")

    def click_on_js_confirm(self):
        BasePage.click_on_element_with_text(self, text="Click for JS Confirm")

    def click_on_js_prompt(self):
        BasePage.click_on_element_with_text(self, text="Click for JS Prompt")

    def click_ok(self):
        BasePage.click_alert_ok(self)

    def click_cancel(self):
        BasePage.click_alert_cancel(self)

    def fill_with(self, text):
        BasePage.fill_alert(self, text)

    def get_result_text(self):
        element = BaseElement.get_preset_element(self.driver, locator=Locator.javascript_alert_result)
        return element.text
