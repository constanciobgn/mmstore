import time

from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


def wait_for_row_in_list_table(context, id_table, row_text):
    start_time = time.time()
    while True:
        try:
            table = context.browser.find_element_by_id(id_table)
            rows = table.find_elements_by_tag_name('tr')
            context.test.assertIn(row_text, [row.text for row in rows])
            return
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)


def wait_for(context, fn):
    start_time = time.time()
    while True:
        try:            
            return fn()
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)

def wait_to_be_logged_in(context, email):
    wait_for(context, lambda: context.browser.find_element_by_link_text('Log out'))
    navbar = context.browser.find_element_by_css_selector('p')
    context.test.assertIn(email, navbar.text)

def wait_to_be_logged_out(context, email):
    wait_for(context, lambda: context.browser.find_element_by_name('email'))
    navbar = context.browser.find_element_by_css_selector('.navbar-custom')
    context.test.assertNotIn(email, navbar.text)