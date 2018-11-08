from forms.models import Item, Form
from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        
class FormViewTest(TestCase):

    def test_uses_form_template(self):
        form_ = Form.objects.create()
        response = self.client.get(f'/forms/{form_.id}/')
        self.assertTemplateUsed(response, 'form.html')

    def test_displays_only_items_for_that_form(self):
        correct_form = Form.objects.create()
        Item.objects.create(text='itemey 1', form=correct_form)
        Item.objects.create(text='itemey 2', form=correct_form)
        other_form = Form.objects.create()
        Item.objects.create(text='other form item 1', form=other_form)
        Item.objects.create(text='other form item 2', form=other_form)
        response = self.client.get(f'/forms/{correct_form.id}/')
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other form item 1')
        self.assertNotContains(response, 'other form item 2')

    def test_passes_correct_form_to_template(self):
        other_form = Form.objects.create()
        correct_form = Form.objects.create()
        response = self.client.get(f'/forms/{correct_form.id}/')
        self.assertEqual(response.context['form'], correct_form)

class FormAndItemModelsTest(TestCase):

    def test_saving_and_retrieving_items(self):
        form_ = Form()
        form_.save()

        first_item = Item()
        first_item.text = 'The first (ever) form item'
        first_item.form = form_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.form = form_
        second_item.save()

        saved_form = Form.objects.first()
        self.assertEqual(saved_form, form_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) form item')

        self.assertEqual(first_saved_item.form, form_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.form, form_)

class NewFormTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/forms/new', data={'item_text': 'A new form item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new form item')


    def test_redirects_after_POST(self):
        response = self.client.post('/forms/new', data={'item_text': 'A new form item'})
        new_form = Form.objects.first()
        self.assertRedirects(response, f'/forms/{new_form.id}/')

class NewItemTest(TestCase):

    def test_can_save_a_POST_request_to_an_existing_form(self):
        other_form = Form.objects.create()
        correct_form = Form.objects.create()

        self.client.post(
            f'/forms/{correct_form.id}/add_item',
            data={'item_text': 'A new item for an existing form'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing form')
        self.assertEqual(new_item.form, correct_form)


    def test_redirects_to_form_view(self):
        other_form = Form.objects.create()
        correct_form = Form.objects.create()

        response = self.client.post(
            f'/forms/{correct_form.id}/add_item',
            data={'item_text': 'A new item for an existing form'}
        )

        self.assertRedirects(response, f'/forms/{correct_form.id}/')
# Create your tests here testds.
