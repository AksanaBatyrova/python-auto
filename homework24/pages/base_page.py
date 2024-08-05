"""Base Page module"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected


class BasePage:
    """Class for basic operations"""

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def find(self, locator):
        return self._wait.until(
            expected.visibility_of_element_located(locator))

    def click(self, locator):
        return self._wait.until(
            expected.element_to_be_clickable(locator)).click()

    def fill(self, locator, text):
        return self._wait.until(
            expected.element_to_be_clickable(locator)).send_keys(text)

    def clear(self, locator):
        return self._wait.until(
            expected.element_to_be_clickable(locator)).clear()

    def wait_for_element(self, locator):
        return self._wait.until(
            expected.presence_of_all_elements_located(locator))

    def get_text(self, locator):
        return self._wait.until(
            expected.visibility_of_element_located(locator)).text

    def get_alert(self):
        return self._wait.until(expected.alert_is_present())

    def accept_alert(self):
        self.get_alert().accept()
