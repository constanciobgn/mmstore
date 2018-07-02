from datetime import date
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from apps.core.models import Item, List, Parcela


class HelloWorldTest(TestCase):

    def test_status_code(self):
        response = self.client.get('/hello/')
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

    def test_can_save_a_POST_request(self):
        self.client.post('/core/lists/new',
                         data={'descricao': 'A new list item', 'cliente': 'Nalveira', 'valor_compra': '50',
                               'data_venda': '01/07/2018', 'status': '0'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.descricao, 'A new list item')
        self.assertEqual(new_item.cliente, 'Nalveira')
        self.assertEqual(new_item.valor_compra, Decimal(50))
        self.assertEqual(new_item.data_venda, date.today())
        self.assertEqual(new_item.status, '0')

    def test_status_code(self):
        list_ = List.objects.create()
        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)
        response = self.client.get(f'/core/lists/{list_.id}/items/{item.id}/add_parcela')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        list_ = List.objects.create()
        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)
        response = self.client.get(f'/core/lists/{list_.id}/items/{item.id}/add_parcela')
        self.assertTemplateUsed(response, 'apps/core/parcela/new.html')

    def test_can_save_a_POST_request(self):
        list_ = List.objects.create()
        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)

        self.client.post(f'/core/lists/{list_.id}/items/{item.id}/add_parcela',
                         data={'data_recebimento': str(date.today()), 'valor': '25', 'status': '0', })

        self.assertEqual(Parcela.objects.count(), 1)

    def test_status_code(self):
        list_ = List.objects.create()
        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)
        response = self.client.get(f'/core/lists/{list_.id}/items/{item.id}')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        list_ = List.objects.create()
        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)
        response = self.client.get(f'/core/lists/{list_.id}/items/{item.id}')
        self.assertTemplateUsed(response, 'apps/core/item_detail.html')





    # def test_status_code(self):
    #     list_ = List.objects.create()
    #     item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
    #                                data_venda=date.today(), status='0', list=list_)
    #     response = self.client.get(f'/core/lists/{list_.id}/items/{item.id}/item_delete')
    #     self.assertEqual(response.status_code, 200)

    def test_item_delete(self):
        list_ = List.objects.create()
        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)
        response = self.client.post(f'/core/lists/{list_.id}/items/{item.id}/item_delete')

        self.assertEqual(Item.objects.count(), 0)