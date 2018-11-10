from unittest import skip
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10

class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def wait_for_row_in_form_table(self, row_text):
        start_time = time.time()
        while True:  
            try:
                table = self.browser.find_element_by_id('id_form_table')  
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return  
            except (AssertionError, WebDriverException) as e:  
                if time.time() - start_time > MAX_WAIT:  
                    raise e  
                time.sleep(10)  

class NewVisitorTest(FunctionalTest):

    def test_can_start_a_form_for_one_user(self):
        # Edith has heard about a cool new online Application Form for app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)
		
        # She notices the page title and header mention Application Form for forms
        self.assertIn('Application forms', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Start a new Application', header_text)

        # She is invited to enter a Application Form for item straight away
        inputbox = self.browser.find_element_by_id('id_new_programName')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a program name for item'
        )

        # She types "Computer Information Systems" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Computer Information Systems')

        # When she hits enter, the page updates, and now the page forms
        # "1: Computer Information Systems" as an item in a Application Form for form table
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_form_table('1: Computer Information Systems')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)

        #inputbox = self.browser.find_element_by_id('id_new_programName')
        #inputbox.send_keys('Use peacock feathers to make a fly')
        #inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her form
        #self.wait_for_row_in_form_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_form_table('1: Computer Information Systems')

    @skip
    def NOest_multiple_users_can_start_forms_at_different_urls(self):
        # Edith starts a new Application Form for form
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_programName')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_form_table('1: Buy peacock feathers')

        # She notices that her form has a unique URL
        edith_form_url = self.browser.current_url
        self.assertRegex(edith_form_url, '/forms/.+')  

        # Now a new user, Francis, comes along to the site.

        # We use a new browser session to make sure that no information
        # of Edith's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page.  There is no sign of Edith's
        # form
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new form by entering a new item. He
        # is less interesting than Edith...
        inputbox = self.browser.find_element_by_id('id_new_programName')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_form_table('1: Buy milk')

        # Francis gets his own unique URL
        francis_form_url = self.browser.current_url
        self.assertRegex(francis_form_url, '/forms/.+')
        self.assertNotEqual(francis_form_url, edith_form_url)

        # Again, there is no trace of Edith's form
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep

class ItemValidationTest(FunctionalTest):

    @skip
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,  
            "You can't have an empty list item"  
        )

        # She tries again with some text for the item, which now works
        self.fail('finish this test!')

        # Perversely, she now decides to submit a second blank list item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')

#if __name__== '__main__':
#		unittest.main(warnings='ignore')