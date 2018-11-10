from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time, re

MAX_WAIT = 10


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)
        job_title_input = self.browser.find_element_by_id('input_27')
        job_title_input.send_keys("SOME_JOB")
        time.sleep(3)
        submit_button = self.browser.find_element_by_id('input_2')
        submit_button.click()
        time.sleep(3)
        text_found = re.search(r'There are errors on the form. Please fix them before continuing.', self.browser.page_source)
        # This should be populated as that means the expression above is True
        self.assertNotEqual(text_found, None)
        time.sleep(3)
