from pages.base_page import Page
from selenium.webdriver.common.by import By

class JobSearchPage(Page):

    _job_qa_locator = (By.XPATH, '//select[@name="category"]/option[@value="%s"]')
    _job_city_locator = (By.XPATH, '//input[@name="search"]')
    _job_checkbox_locator = (By.XPATH, '//input[@type="checkbox" and contains (@name, "descr")]')
    _job_find_button_locator = (By.XPATH, '//input[@class="btn-search"]')
    _job_header_locator = (By.XPATH, '//div[@class="b-inner-page-header"]')

    def choose_job(self, position):
        self.element_click(self._job_qa_locator, position)

    def fill_in_location(self, location):
        self.element_click(self._job_city_locator)
        self.element_clear(self._job_city_locator)
        self.element_send_keys(self._job_city_locator, location)

    def click_checkbox(self):
        self.element_click(self._job_checkbox_locator)

    def click_find_button(self):
        self.element_click(self._job_find_button_locator)

    def check_header_contains_digits(self):
        job_header_digits = self._job_header_locator.text
        job_header_digits.split(' ')
        job_header_digits[0].isdigit()
