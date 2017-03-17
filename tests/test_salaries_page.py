from selenium import webdriver
from pages.home_page import Header
from pages.salaries_page import SalariesPage
from data.urls import url

from data.locations import locations

class TestSalaries():

    @classmethod
    def setup(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(url)

    @classmethod
    def teardown(cls):
        cls.driver.quit()

    def test_job_search_header(self):
        Header(self.driver).\
            click_jobs_search_menu()
        salaries_page = SalariesPage(self.driver)
        salaries_page.choose_location()
        salaries_page.choose_position()
        salaries_page.choose_specialization()
        assert salaries_page._salaries_result_locator is not None