from selenium import webdriver
import time, re

from abet_form.models import Application, User


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
        str_lookup = []
        self.update_program_name("Some Program")
        str_lookup.append("Some Program")
        self.update_contact_phone("1112223456")
        str_lookup.append("1112223456")
        self.update_job_title("Some Title")
        str_lookup.append("Some Title")
        self.update_po("SOME PO")
        str_lookup.append("SOME PO")
        self.click_first_program_type()
        str_lookup.append("Some Program")
        self.click_acknowledge()
        str_lookup.append("Some Program")
        self.click_first_so()
        str_lookup.append("Some Program")
        return str_lookup

    '''
        Create Various Functions
    '''

    def create_dummy_applications(self, user=None):
        list_id = []
        if user is None:
            print("User Count -> %s" % User.objects.all().count())
            raise Exception("You Need to Specify Valid User")
        for i in range(0, 10, 1):
            app = Application()
            app.user = user
            app.save()
            list_id.append(app.id)
        return list_id

    '''
        Click the Submit Button on the Page
    '''

    def click_submit(self):
        self.browser.find_element_by_id('input_2').click()

    '''
        Find Error Message on Page
    '''

    def get_submit_error(self):
        return re.search(r'There are errors on the form. Please fix them before continuing.', self.browser.page_source)

    '''
        Scroll to Bottom of Page
    '''

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
