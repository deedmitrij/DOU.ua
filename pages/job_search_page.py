from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from data.urls import urls

class BasePage():
    def __init__(self, driver):
        self.driver = driver

class Header(BasePage):

    def click_calendar_menu(self):
        self.driver.find_element_by_xpath('//a[contains(text(), "Календарь")]').click()

    def click_jobs_search_menu(self):
        self.driver.find_element_by_xpath('//a[contains(text(), "Работа")]').click()

    def click_salaries_menu(self):
        self.driver.find_element_by_xpath('//a[contains(text(), "Зарплаты")]').click()

class JobSearchPage(BasePage):
    def checking_digits_in_header(self):
        self.job = browser.find_element_by_xpath('//a[contains(text(), "Работа")]').click()
        self.job_qa = browser.find_element_by_xpath('//select[@name="category"]/option[@value="QA"]').click()
        self.job_city = browser.find_element_by_xpath('//input[@name="search"]').send_keys('Київ')
        self.job_checkbox = browser.find_element_by_xpath('//input[@type="checkbox" and contains (@name, "descr")]').click()
        self.job_find_button = browser.find_element_by_xpath('//input[@class="btn-search"]').click()
        self.job_header = browser.find_element_by_xpath('//div[@class="b-inner-page-header"]').text
        self.job_header_digits = self.job_header.split(' ')
		job_header_digits = job_header.split(' ')
        assert job_header_digits[0].isdigit() == True

class TestEvent():

    @classmethod
    def setup(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://dou.ua/')

    @classmethod
    def teardown(cls):
        cls.driver.quit()

    def test_event_created(self):
        assert JobSearchPage(self.driver).event_created() == True