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

class CalendarPage(BasePage):
    def event_created(self):
        Header(self.driver).click_calendar_menu()
        self.driver.find_element_by_xpath('//a[@href="https://dou.ua/calendar/add/"]').click()
        self.driver.find_element_by_xpath('//input[@name="title"]').send_keys('Test')
        self.driver.find_element_by_xpath('//input[@name="cost"]').send_keys('500')
        self.driver.find_element_by_xpath('//input[@name="place"]').send_keys('Kyiv')
        self.driver.find_element_by_xpath('//textarea[@name="content"]').send_keys('Test')
        self.driver.find_element_by_xpath('//button[@id="btnSubmit"]').click()
        return 'Событие было отправлено на проверку модераторам сайта' in self.driver.page_source

class TestEvent():

    @classmethod
    def setup(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://dou.ua/')

    @classmethod
    def teardown(cls):
        cls.driver.quit()

    def test_event_created(self):
        assert CalendarPage(self.driver).event_created() == True