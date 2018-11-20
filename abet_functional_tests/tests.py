from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from abet_form.models import User, Application
from abet_form_utils import abet_form_utils
import time, re

MAX_WAIT = 10


class FailureFormSubmissions(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.abet_form_util = abet_form_utils.abet_form_util(self.browser)
    '''
    Feature: Application failed to be stored (Fail Adding Incomplete Application)  
    Scenario:  
        User fills out application  
        Given submit button is clicked on application  
        When the form validation finds an input error  
        The program will not store the application   
        And notify the user of the input error  
    '''
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

    def tearDown(self):
        Application.objects.all().delete()
        self.assertEqual(Application.objects.count(), 0)
        User.objects.all().delete()
        self.assertEqual(User.objects.count(), 0)
        pass
        self.browser.quit()


class SuccessFormSubmissions(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.abet_form_util = abet_form_utils.abet_form_util(self.browser)

    def tearDown(self):
        Application.objects.all().delete()
        self.assertEqual(Application.objects.count(), 0)
        User.objects.all().delete()
        self.assertEqual(User.objects.count(), 0)
        self.browser.quit()

    '''
    Feature: Application is stored to database (Add Complete Application)  
    Scenario:  
        User fills out application  
        Given Submit button is clicked on application  
        When the form passes all required field validation  
        The program will create a record in database with the data from the application  
    '''
    def test_valid_form(self):
        self.browser.get(self.live_server_url)
        self.abet_form_util.fill_valid_form()

        time.sleep(3)

        # If we don't scroll to the botton the page the footer overlap the submit button
        self.abet_form_util.scroll_to_bottom_of_page()
        time.sleep(3)
        # Click submit button
        self.abet_form_util.click_submit()
        time.sleep(3)
        # This should be populated as that means the error expression True
        self.assertEqual(self.abet_form_util.get_submit_error(), None)
