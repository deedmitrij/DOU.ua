from pages.base_page import Page
from selenium.webdriver.common.by import By

class SalariesPage():

    _salaries_city_locator = (By.XPATH, '//select[@name="city"]/option[@value="all"]')
    _salaries_position_locator = (By.XPATH, '//select[@name="title"]/optgroup[@label="QA"]/option[contains(text(), "Junior QA engineer")]')
    _salaries_specialization_locator = (By.XPATH, '//select[@name="spec"]/option[contains(text(), "Automation QA")]')
    _salaries_result_locator = (By.XPATH, '//dl[@class="salarydec-results"]/dd[@class="salarydec-results-min"]/span[@class="num"]')

    def choose_location(self):
        self.element_click(self._salaries_city_locator)

    def choose_position(self):
        self.element_click(self._salaries_position_locator)

    def choose_specialization(self):
        self.element_click(self._salaries_specialization_locator)

sd
