from pytest import mark
from pages.home import *
from pages.javascript_alerts import *
from resources.requirements import *


class TestDropdown:

    @mark.regression
    @mark.ui
    def test_js_alert(self, chrome_browser, main_url):

        chrome_browser.get(main_url)
        main_page = Home(chrome_browser)
        main_page.click_on_javascript_alerts()

        javascript_alerts = JSAlerts(chrome_browser)
        javascript_alerts.click_on_js_alert()
        javascript_alerts.click_ok()

        result = javascript_alerts.get_result_text()
        expected_result = Req.ALERT_SUCCESSFUL_CLICK

        assert expected_result == result

    @mark.regression
    @mark.ui
    def test_js_confirm_ok(self, chrome_browser, main_url):

        chrome_browser.get(main_url)
        main_page = Home(chrome_browser)
        main_page.click_on_javascript_alerts()

        javascript_alerts = JSAlerts(chrome_browser)
        javascript_alerts.click_on_js_confirm()
        javascript_alerts.click_ok()

        result = javascript_alerts.get_result_text()
        expected_result = Req.ALERT_CONFIRM_OK

        assert expected_result == result

    @mark.regression
    @mark.ui
    @mark.negative
    def test_js_confirm_cancel(self, chrome_browser, main_url):
        chrome_browser.get(main_url)
        main_page = Home(chrome_browser)
        main_page.click_on_javascript_alerts()

        javascript_alerts = JSAlerts(chrome_browser)
        javascript_alerts.click_on_js_confirm()
        javascript_alerts.click_cancel()

        result = javascript_alerts.get_result_text()
        expected_result = Req.ALERT_CONFIRM_CANCEL

        assert expected_result == result

    @mark.regression
    @mark.ui
    def test_js_prompt(self, chrome_browser, main_url):
        chrome_browser.get(main_url)
        main_page = Home(chrome_browser)
        main_page.click_on_javascript_alerts()

        javascript_alerts = JSAlerts(chrome_browser)
        javascript_alerts.click_on_js_prompt()
        fill_text = "text info"
        javascript_alerts.fill_with(fill_text)
        javascript_alerts.click_ok()

        result = javascript_alerts.get_result_text()
        expected_result = Req.ALERT_FILL % fill_text

        assert expected_result == result
