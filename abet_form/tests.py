from django.core import serializers
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from abet_form.views import home_page
from abet_form.views_crud import test_routing
from abet_form.models import Application, User
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        print("Starting test_uses_home_template")
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class Test_GET_Method(TestCase):
    # Ensure, for testing purposes, that we only have a single user in the system
    def setUp(self):
        self.assertEqual(User.objects.count(), 1)

    # Test that we don't support creating applications using a GET call
    def test_crud_create_application(self):
        l_user = User.objects.first()
        url = "/abet_form/%s/add_application" % l_user.uuid_id
        response = self.client.get(url)
        self.assertIn('Sorry, we don\'t support application GET submissions', response.content.decode())

    # remove all users and applications form the system
    def tearDown(self):
        Application.objects.all().delete()
        self.assertEqual(Application.objects.count(), 0)
        User.objects.all().delete()
        self.assertEqual(User.objects.count(), 0)


class Test_POST_Method(TestCase):

    # Ensure, for testing purposes, that we only have a single user in the system
    def setUp(self):
        self.assertEqual(User.objects.count(), 1)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('home.html')
        self.assertEqual(html, expected_html)

    def test_correct_url_routing(self):
        request = HttpRequest()
        response = test_routing(request)
        html = response.content.decode('utf8')
        expected_html = r'YAY we actually work!!!'
        self.assertEqual(html, expected_html)

    def test_simple_post_method(self):
        response = self.client.post('/abet_form/test_simple_url_post', data={'key': 'value'})
        self.assertIn('=====you_reached_a_post=====', response.content.decode())

    def test_crud_create_application(self):
        l_user = User.objects.first()
        url = "/abet_form/%s/add_application" % l_user.uuid_id
        response = self.client.post(url, data={'user_id': l_user})
        # Ensure that only one application has been added
        self.assertEqual(Application.objects.all().count(), 1)
        # Ensure that we display the webpage as expected
        self.assertTemplateUsed(response, 'details.html')

    def test_crud_read_function(self):
        l_user = User.objects.first()
        n_app = Application(user=l_user)
        n_app.save()
        url = "/abet_form/%s/get_application" % n_app.id
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'details.html')
        self.assertContains(response, n_app.id)

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
        n_app.job_title = "I have been updated"
        response = self.client.post('/abet_form/update_application', data={"id" : n_app.id, "job_title": n_app.job_title})
        self.assertContains(response, "I have been updated")

    # add a application and use the delete url to remove it
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
        User.objects.all().delete()
        self.assertEqual(User.objects.count(), 0)
