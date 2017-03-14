from selenium import webdriver
from pages.home_page import Header
from pages.calendar_page import CalendarPage
from data.urls import url
from data.titles import title
from data.descriptions import description
from data.locations import location
from data.prices import price

class TestEventCreated():

    @classmethod
    def setup(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://dou.ua/')

    @classmethod
    def teardown(cls):
        cls.driver.quit()

    def test_event_created(self):
        Header.click_calendar_menu()
        assert CalendarPage.check_message() == True
