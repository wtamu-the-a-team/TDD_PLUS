from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from abet_form.views import home_page
from abet_form.views_crud import test_routing
from abet_form.models import Application, User
from django.template.loader import render_to_string


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class Test_POST_Method(TestCase):

    def setUp(self):
        user = User()
        user.save()
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

    def test_can_save_a_POST_request(self):
        response = self.client.post('/abet_form/test_post', data={'item_text': 'A new list item'})
        self.assertIn('=====you_reached_a_post=====', response.content.decode())

    def test_simple_post_method(self):
        # print("Sending a Simple POST to root")
        # first_item = Application()
        # first_item.contact_name = "some_name"
        # first_item.save()
        #
        # second_item = Application()
        # second_item.contact_name = "some_other_name"
        # second_item.save()

        saved_items = Application.objects.all()
        print("=====%s=====" % saved_items.count())

    def test_post_add_application(self):
        object_to_post = ""

    def tearDown(self):
        Application.objects.all().delete()
        self.assertEqual(Application.objects.count(), 0)
        User.objects.all().delete()
        self.assertEqual(User.objects.count(), 0)
