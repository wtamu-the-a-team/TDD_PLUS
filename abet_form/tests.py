from django.core import serializers
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from abet_form.abet_model_utils import abet_model_utils
from abet_form.abet_model_utils.abet_model_utils import get_simple_post_response, dumb_success_message, \
    success_update_message
from abet_form.views import home_page
from abet_form.views_crud import test_routing
from abet_form.models import Application, User
from django.template.loader import render_to_string


class HomePageTest(TestCase):
    '''
    Feature: (Test Root Page Returns Home)
    Scenario:
        Given a user requests the root
        When the get method is called on
        The method will return a correctly rendered home page
    '''

    def test_uses_home_template(self):
        # print("Starting test_uses_home_template")
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class Test_GET_Method(TestCase):
    # Ensure, for testing purposes, that we only have a single user in the system
    def setUp(self):
        self.assertEqual(User.objects.count(), 1)

    '''
    Feature: (Test Attempted Add Application using GET Call)  
    Scenario:  
        Given a user requests the Add URL using a GET Call 
        When the get method is called on  
        The method will return an error message 
    '''

    def test_crud_create_application(self):
        l_user = User.objects.first()
        url = "/abet_form/%s/add_application" % l_user.uuid_id
        response = self.client.get(url)
        self.assertIn('Sorry, we don\'t support application GET submissions', response.content.decode())

    '''
    Feature: (Test Attempted Add Application using GET Call)  
    Scenario:  
        Given a user requests the Add URL using a GET Call 
        When the get method is called on  
        The method will return an error message 
    '''

    def test_crud_retieve_unknown(self):
        url = "/abet_form/%s/get_application" % "00000000-0000-0000-0000-000000000000"
        response = self.client.get(url)
        self.assertIn(abet_model_utils.get_unknown_application_id_error(), response.content.decode())

    # remove all users and applications form the system
    def tearDown(self):
        Application.objects.all().delete()
        self.assertEqual(Application.objects.count(), 0)
        # User.objects.all().delete()
        # self.assertEqual(User.objects.count(), 0)


class Test_POST_Method(TestCase):

    # Ensure, for testing purposes, that we only have a single user in the system
    def setUp(self):
        self.assertEqual(User.objects.count(), 1)

    '''
    Feature: (Test Return Root Page)  
    Scenario:  
        Given a user requests the homepage 
        When the get method is called on  
        The method will return a correctly rendered root page 
    '''

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    '''
    Feature: (Test Return Home Page)  
    Scenario:  
        Given a user requests the homepage 
        When the get method is called on  
        The method will return a correctly rendered home  
    '''

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('home.html')
        self.assertEqual(html, expected_html)

    '''
    Feature: (Test URL GET Routing)  
    Scenario:  
        Given an existing application was selected from the list  
        When the get method is called on  
        The method will print “Pass” to the console  
    '''

    def test_correct_url_routing(self):
        request = HttpRequest()
        response = test_routing(request)
        html = response.content.decode('utf8')
        expected_html = dumb_success_message()
        self.assertEqual(html, expected_html)

    '''
    Feature: (Test URL POST Routing)  
    Scenario:  
        Given a new application was submitted  
        When the post method directs to the correct URL method  
        The method will print “Pass” to the console 
    '''

    def test_simple_post_method(self):
        response = self.client.post('/abet_form/test_simple_url_post', data={'key': 'value'})
        self.assertIn(get_simple_post_response(), response.content.decode())

    '''
    Feature: Add functionality executing correctly (Add Application)  
    Scenario:   
        Given application was submitted	  
        When a new application object is created  
        And all data is saved to the database  
        The application will be redirected to the details page  
        And print “Pass” to the console  
    '''

    def test_crud_create_application(self):
        l_user = User.objects.first()
        url = "/abet_form/%s/add_application" % l_user.uuid_id
        response = self.client.post(url, data={'user_id': l_user})
        # Ensure that only one application has been added
        self.assertEqual(Application.objects.all().count(), 1)
        # Ensure that we display the webpage as expected
        self.assertTemplateUsed(response, 'details.html')

    '''
    Feature: (Test Failing Duplicate Application Add)  
    Scenario:  
        Given an application has been submitted  
        When a duplicate application is added to the database  
        The method will print a notification to the console 
    '''

    def test_crud_create_application(self):
        l_user = User.objects.first()
        url = "/abet_form/%s/add_application" % l_user.uuid_id
        response = self.client.post(url, data={'user_id': l_user})
        # Ensure that only one application has been added
        self.assertEqual(Application.objects.all().count(), 1)
        # Ensure that we display the webpage as expected
        app = Application.objects.first()
        self.assertRedirects(response, f'/abet_form/{app.id}/get_application')

    '''
    Feature: Read functionality executing correctly (Read Application)  
    Scenario:  
        Given the application details page is redirected to  
        When the object is retrieved   
        And all the data is stored to a variable  
        And the variable is rendered to the details page  
        The data will be displayed on the details page  
        And print “Pass” to the console  
    '''

    def test_crud_read_function(self):
        l_user = User.objects.first()
        n_app = Application(user=l_user)
        n_app.save()
        url = "/abet_form/%s/get_application" % n_app.id
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'details.html')
        self.assertContains(response, n_app.id)

    '''    
    Feature: Edit functionality executing correctly (Edit Application)  
    Scenario:  
        Given the application is submitted form the edit page  
        When the object is retrieved   
        And all fields are saved to the existing record  
        The application will be redirected to the details page  
        And print “Pass” to the console 
    '''

    def test_crud_update_function(self):
        l_user = User.objects.first()
        n_app = Application(user=l_user)
        n_app.job_title = "I contain no updates"
        n_app.save()
        url = "/abet_form/%s/get_application" % n_app.id
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'details.html')
        self.assertContains(response, n_app.id)
        self.assertContains(response, n_app.job_title)
        n_app.job_title = success_update_message()
        response = self.client.post('/abet_form/update_application',
                                    data={"id": n_app.id, "job_title": n_app.job_title})
        self.assertContains(response, success_update_message())

    '''
    Feature: Delete functionality executing correctly (Delete Application)  
    Scenario:  
        Given the application delete button is clicked  
        When the application record has been removed from the database  
        The application will be redirected to the list of applications created by the user  
        And print “Pass” to the console  
    '''

    def test_crud_delete_function(self):
        l_user = User.objects.first()
        n_app = Application(user=l_user)
        n_app.save()
        app = Application.objects.filter(user=l_user).first()
        url = "/abet_form/%s/remove_application" % app.id
        response = self.client.post(url)
        s_app = Application.objects.filter(id=n_app.id).first()
        self.assertEqual(s_app, None)

    # remove all users and applications form the system
    def tearDown(self):
        Application.objects.all().delete()
        self.assertEqual(Application.objects.count(), 0)
        # User.objects.all().delete()
        # self.assertEqual(User.objects.count(), 0)
