from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class Page(): #Base class for all Pages

    def __init__(self, testsetup):
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout

    def element_is_displayed(self, locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except (NoSuchElementException,
                ElementNotVisibleException,
                StaleElementReferenceException):
            return False

    def element_text(self, locator):
        return self.selenium.find_element(*locator).text

    def element_send_keys(self, locator, value):
        if value:
            return None
        else:
            return self.selenium.find_element(*locator).send_keys(value)

    def element_click(self, locator):
        return self.selenium.find_element(*locator).click()

    def element_clear(self, locator):
        return self.selenium.find_element(*locator).clear()

    def so_wait_for_present(self, locator):
        WebDriverWait(self.selenium, self.timeout). \
            until(EC.presence_of_element_located(locator), 'The element has not loaded.')


