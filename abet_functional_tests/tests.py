from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time, re

MAX_WAIT = 10

class abet_form_util:

    def __init__(self, browser):
        self.browser = browser

    def get_program_name(self):
        pass

    def get_contact_name(self):
        pass

    def get_job_title_element(self):
        return self.browser.find_element_by_id('input_27')

    def update_job_title(self, text):
        self.get_job_title_element().send_keys(text)

    def get_job_title(self):
        return self.browser.find_element_by_id('input_27').text

    def click_submit(self):
        self.browser.find_element_by_id('input_2').click()

    def get_submit_error(self):
        return re.search(r'There are errors on the form. Please fix them before continuing.', self.browser.page_source)

    def scroll_to_bottom_of_page(self):
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = self.browser.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.abet_form_util = abet_form_util(self.browser)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)
        self.abet_form_util.update_job_title("SOME_JOB")
        # If we don't scroll to the botton the page the footer overlap the submit button
        self.abet_form_util.scroll_to_bottom_of_page()
        time.sleep(3)
        self.abet_form_util.click_submit()
        time.sleep(3)
        # This should be populated as that means the expression above is True
        self.assertNotEqual(self.abet_form_util.get_submit_error(), None)
        time.sleep(3)
