from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):

    _calendar_menu_locator = (By.XPATH, '//a[contains(text(), "Календарь")]')
    _jobs_search_menu_locator = (By.XPATH, '//a[contains(text(), "Работа")]')
    _salaries_menu_locator = (By.XPATH, '//a[contains(text(), "Зарплаты")]')

    def click_calendar_menu(self):
        self.element_click(self._calendar_menu_locator)

    def click_jobs_search_menu(self):
        self.element_click(self._jobs_search_menu_locator)

    def click_salaries_menu(self):
        self.element_click(self._jobs_search_menu_locator)/
