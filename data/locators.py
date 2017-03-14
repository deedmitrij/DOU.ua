class CalendarPage_locators():
    calendar = '//a[contains(text(), "Календарь")]'
    add_event = '//a[@href="https://dou.ua/calendar/add/"]'
    event_title = '//input[@name="title"]'
    event_price = '//input[@name="cost"]'
    event_location = '//input[@name="place"]'
    event_description = '//textarea[@name="content"]'
    event_send_button = '//button[@id="btnSubmit"]'
    event_check_message = 'Событие было отправлено на проверку модераторам сайта'

class JobSearchPage_locators():
    job = '//a[contains(text(), "Работа")]'
    job_qa = '//select[@name="category"]/option[@value="QA"]'
    job_city = '//input[@name="search"]'
    job_checkbox = '//input[@type="checkbox" and contains (@name, "descr")]'
    job_find_button = '//input[@class="btn-search"]'
    job_header = '//div[@class="b-inner-page-header"]'

class SalariesPage_locators():
    salaries = '//a[contains(text(), "Зарплаты")]'
    salaries_city = '//select[@name="city"]/option[@value="all"]'
    salaries_position = '//select[@name="title"]/optgroup[@label="QA"]/option[contains(text(), "Junior QA engineer")]'
    salaries_specialization = '//select[@name="spec"]/option[contains(text(), "Automation QA")]'
    salaries_result = '//dl[@class="salarydec-results"]/dd[@class="salarydec-results-min"]/span[@class="num"]'