from django.test import TestCase
from abet_form.models import Application, Abet_Form


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class Test_POST_Method(TestCase):

    def test_simple_post_method(self):
        print("Sending a Simple POST to root")
        Abet_Form.objects
        self.client.post('/')