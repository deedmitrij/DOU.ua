
def fill_in_calendar_form(page, price='20', title='test event', location='Kiev', description=''):
    page.fill_in_price(price)
    page.fill_in_description(description)
    page.fill_in_title(title)
    page.fill_in_location(location)

def fill_in_job_search_form(page, location='Київ'):
    page.fill_in_location(location)


