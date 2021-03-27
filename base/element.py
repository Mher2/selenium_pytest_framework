from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from resources.constants import *


class BaseElement(object):

    @staticmethod
    def get_visible_element(driver, locator):
        element = WebDriverWait(driver, TIMEOUT).until(
            ec.visibility_of_element_located((By.XPATH, locator))
        )
        return element

    @staticmethod
    def get_preset_element(driver, locator):
        element = WebDriverWait(driver, TIMEOUT).until(
            ec.presence_of_element_located((By.XPATH, locator))
        )
        return element

    @staticmethod
    def get_visible_elements(driver, locator):
        elements = WebDriverWait(driver, TIMEOUT).until(
            ec.visibility_of_all_elements_located((By.XPATH, locator))
        )
        return elements

    @staticmethod
    def get_select_element(driver, locator):
        select = Select(WebDriverWait(driver, TIMEOUT).until(ec.element_to_be_clickable((By.XPATH, locator))))
        return select

    @staticmethod
    def get_popup_element(driver):
        element = WebDriverWait(driver, TIMEOUT).until(ec.alert_is_present())
        return element
