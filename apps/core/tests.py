from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .forms import ItemForm
from .models import List, Item


class HelloWorldTest(TestCase):

    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 200)


class MMStoreAdminTest(TestCase):

    def test_status_code(self):
        response = self.client.get('/core/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('mmstore_admin'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('mmstore_admin'))
        self.assertTemplateUsed(response, 'apps/core/index.html')

    def test_view_not_uses_incorrect_template(self):
        response = self.client.get(reverse('mmstore_admin'))
        self.assertTemplateNotUsed(response, 'apps/core/fake.html')

    def test_home_page_uses_item_form(self):
        response = self.client.get(reverse('mmstore_admin'))
        self.assertIsInstance(response.context['form'], ItemForm)

    def test_form_item_input_has_placeholder_and_css_classes(self):
        form = ItemForm()
        self.assertIn('id="id_descricao"', form.as_p())
        self.assertIn('id="id_valor_compra"', form.as_p())
        self.assertIn('id="id_data_venda"', form.as_p())

    def test_saving_and_retrieving_items(self):
        list_ = List.objects.create()
        Item.objects.create(descricao='The first list item', valor_compra=Decimal(50), list=list_)

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 1)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.descricao, 'The first list item')
        self.assertEqual(first_saved_item.valor_compra, Decimal(50))
        self.assertEqual(first_saved_item.list, list_)

    def test_can_save_a_POST_request(self):
        self.client.post('/core/lists/new', data={'descricao': 'A new list item', 'valor_compra': '50'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.descricao, 'A new list item')
        self.assertEqual(new_item.valor_compra, Decimal(50))
