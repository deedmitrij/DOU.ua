import pytest

from selenium import webdriver
from pages.home_page import Header
from pages.calendar_page import CalendarPage
from steps.steps import fill_in_calendar_form
from data.titles import title
from data.descriptions import description
from data.locations import locations
from data.prices import prices
from data.urls import url

class TestEventCreated():

    @classmethod
    def setup(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(url)

    @classmethod
    def teardown(cls):
        cls.driver.quit()

    @pytest.mark.parametrize('location', locations)
    @pytest.mark.parametrize('price', prices)
    def test_event_created(self, price, location):
        Header(self.driver).\
            click_calendar_menu()
        calendar_page = CalendarPage(self.driver)
        calendar_page.click_add_event_button()
        fill_in_calendar_form(calendar_page, price, 'TEST EVENT CREATED', location, 'HELLO ADMIN')
        calendar_page.click_send_button()
        assert calendar_page.check_result_message() == True
