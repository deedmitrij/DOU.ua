import pytest

from selenium import webdriver
from pages.home_page import Header
from pages.job_search_page import JobSearchPage
from steps.steps import *
from data.job_search_positions import positions
from data.urls import url

from data.locations import locations

class TestJobHeader():

    @classmethod
    def setup(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(url)

    @classmethod
    def teardown(cls):
        cls.driver.quit()

    @pytest.mark.parametrize('position', positions)
    @pytest.mark.parametrize('location', locations)
    def test_job_search_header(self, position, location):
        Header(self.driver).\
            click_jobs_search_menu()
        job_search_page = JobSearchPage(self.driver)
        job_search_page.choose_job(position)
        fill_in_job_search_form(job_search_page, location)
        job_search_page.click_checkbox()
        job_search_page.click_find_button()
        assert job_search_page.check_header_contains_digits() == True