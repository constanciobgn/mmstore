from django.test import TestCase
from django.urls import reverse


class HelloWorldTest(TestCase):

    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 200)
