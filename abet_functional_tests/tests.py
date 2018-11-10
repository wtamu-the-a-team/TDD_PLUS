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

    '''
        Job Title Elements
    '''
    def get_job_title_element(self):
        return self.browser.find_element_by_id('input_27')

    def update_job_title(self, text):
        self.get_job_title_element().send_keys(text)

    def get_job_title(self):
        return self.get_job_title_element().text

    '''
        Program Name Elements
    '''
    def get_program_name_element(self):
        return self.browser.find_element_by_id('input_9')

    def update_program_name(self, text):
        self.get_program_name_element().send_keys(text)

    def get_program_name(self):
        return self.get_program_name_element().text

    '''
        Contact Phone Elements
    '''
    def get_contact_phone_element(self):
        return self.browser.find_element_by_id('input_13')

    def update_contact_phone(self, text):
        self.get_contact_phone_element().send_keys(text)

    def get_contact_phone(self):
        return self.get_contact_phone_element().text

    '''
        Acknowledgement
    '''
    def click_acknowledge(self):
        self.browser.find_element_by_id('input_25_0').click()

    '''
        Program Educational Objectives Elements
    '''
    def get_po_element(self):
        return self.browser.find_element_by_id('input_16')

    def update_po(self, text):
        self.get_po_element().send_keys(text)

    def get_po(self):
        return self.get_po_element().text

    '''
        Student Outcomes
    '''
    def click_first_so(self):
        self.browser.find_element_by_id('input_22_0').click()

    '''
        Program Type
    '''
    def click_first_program_type(self):
        self.browser.find_element_by_id('input_19_0').click()

    '''
        Various Functions
    '''
    def fill_valid_form(self):
        self.update_program_name("Some Program")
        self.update_contact_phone("1112223456")
        self.update_job_title("Some Title")
        self.update_po("SOME PO")
        self.click_first_program_type()
        self.click_acknowledge()
        self.click_first_so()

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

    def test_invalid_form(self):
        self.browser.get(self.live_server_url)
        self.abet_form_util.update_job_title("SOME_JOB")
        self.abet_form_util.update_contact_phone("1112223456")
        self.abet_form_util.update_program_name("some_program")

        time.sleep(3)
        # Click submit button
        self.abet_form_util.click_submit()
        time.sleep(3)
        # If we don't scroll to the botton the page the footer overlap the submit button
        self.abet_form_util.scroll_to_bottom_of_page()
        time.sleep(3)
        # This should be populated as that means the error expression True
        self.assertNotEqual(self.abet_form_util.get_submit_error(), None)

    def test_valid_form(self):
        self.browser.get(self.live_server_url)
        self.abet_form_util.fill_valid_form()

        time.sleep(3)
        # Click submit button
        self.abet_form_util.click_submit()
        time.sleep(3)
        # If we don't scroll to the botton the page the footer overlap the submit button
        self.abet_form_util.scroll_to_bottom_of_page()
        time.sleep(3)
        # This should be populated as that means the error expression True
        self.assertEqual(self.abet_form_util.get_submit_error(), None)
