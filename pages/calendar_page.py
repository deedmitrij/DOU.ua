from pages.base_page import Page
from selenium.webdriver.common.by import By

class CalendarPage(Page):

    _add_event_locator = (By.XPATH, '//a[@href="https://dou.ua/calendar/add/"]')
    _event_title_locator = (By.XPATH, '//input[@name="title"]')
    _event_price_locator = (By.XPATH, '//input[@name="cost"]')
    _event_location_locator = (By.XPATH, '//input[@name="place"]')
    _event_description_locator = (By.XPATH, '//textarea[@name="content"]')
    _event_send_button_locator = (By.XPATH, '//button[@id="btnSubmit"]')
    _event_check_message = 'Событие было отправлено на проверку модераторам сайта'

    def click_add_event_button(self):
        self.element_click(self._add_event_locator)

    def fill_in_title(self, title):
        self.element_click(self._event_title_locator)
        self.element_clear(self._event_title_locator)
        self.element_send_keys(self._event_title_locator, title)

    def fill_in_price(self, price):
        self.element_click(self._event_price_locator)
        self.element_clear(self._event_price_locator)
        self.element_send_keys(self._event_price_locator, price)

    def fill_in_location(self, location):
        self.element_click(self._event_location_locator)
        self.element_clear(self._event_location_locator)
        self.element_send_keys(self._event_location_locator, location)

    def fill_in_description(self, description):
        self.element_click(self._event_description_locator)
        self.element_clear(self._event_description_locator)
        self.element_send_keys(self._event_description_locator, description)

    def click_send_button(self):
        self.element_click(self._event_send_button_locator)

    def check_result_message(self):
        return self._event_check_message in self.driver.page_source
