from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from web.models import Library, Scenario
from web.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


    def test_home_page_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())


    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')


    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')


    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)



class LibraryModelTest(TestCase):

    def setup(self):
        # add some scenarios
        self.s1 = Scenario.objects.create(name="poor light")
        self.s2 = Scenario.objects.create(name="jumping")
        self.s3 = Scenario.objects.create(name="outdoors")
        self.s4 = Scenario.objects.create(name="one horse")

    def test_saving_and_retrieving_items(self):


        v1 = Library()
        v1.ref = 'Video 1'
        v1.save()
        v1.scenarios.add(self.s1,self.s2)

        v2 = Library()
        v2.text = 'Video 2'
        v2.save()
        v2.scenarios.add(self.s3)

        saved_items = Library.objects.all()
        self.assertEqual(saved_items.count(), 2)

        v1 = saved_items[0]
        v2 = saved_items[1]
        self.assertEqual(v1.text, 'Video 1')
        self.assertEqual(v2.text, 'Video 2')
