from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class Page(): #Base class for all Pages

    def __init__(self, driver):
        self.driver = driver


    def element_is_displayed(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except (NoSuchElementException,
                ElementNotVisibleException,
                StaleElementReferenceException):
            return False

    def element_text(self, locator):
        return self.driver.find_element(*locator).text

    def element_send_keys(self, locator, value):
        if not value:
            return None
        else:
            return self.driver.find_element(*locator).send_keys(value)

    def element_click(self, locator):
        return self.driver.find_element(*locator).click()

    def element_clear(self, locator):
        return self.driver.find_element(*locator).clear()/
