from datetime import date, timedelta
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from apps.core.forms import PrecoForm
from apps.core.models import Item, List, Parcela


class HelloWorldTest(TestCase):

    def test_status_code(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 200)


class NewListTest(TestCase):

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
                               'data_venda': f'{ date.today().strftime("%d/%m/%Y") }', 'status': '0'})

        self.assertEqual(Item.objects.count(), 1)

        new_item = Item.objects.first()
        self.assertEqual(new_item.descricao, 'A new list item')
        self.assertEqual(new_item.cliente, 'Nalveira')
        self.assertEqual(new_item.valor_compra, Decimal(50))
        self.assertEqual(new_item.data_venda, date.today())
        self.assertEqual(new_item.status, '0')

    def test_redirects_after_POST(self):
        response = self.client.post('/core/lists/new',
                                    data={'descricao': 'A new list item', 'cliente': 'Nalveira', 'valor_compra': '50',
                                          'data_venda': '01/07/2018', 'status': '0'})

        self.assertRedirects(response, '/core/')

    def test_view_returns_items(self):
        list_ = List.objects.create()
        Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                            data_venda=date.today(), status='0', list=list_)

        response = self.client.get('/core/')
        self.assertQuerysetEqual(response.context['items'], ['<Item: Item object (1)>'])

    def test_view_returns_items_com_parcelas_atrasadas(self):
        list_ = List.objects.create()

        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)

        Parcela.objects.create(data_recebimento=date.today(), valor=Decimal(25), status='0', item=item)

        item = Item.objects.create(descricao='Blusa vermelha', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)

        Parcela.objects.create(data_recebimento=date.today() - timedelta(days=1), valor=Decimal(25), status='0',
                               item=item)

        saved_parcelas = Parcela.objects.all()
        self.assertEqual(saved_parcelas.count(), 2)

        response = self.client.get('/core/')
        self.assertQuerysetEqual(response.context['items_atrasados'], ['<Item: Item object (2)>'])


class MMStoreAdminTest(TestCase):

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

        self.client.post(f'/core/lists/{list_.id}/items/{item.id}/item_delete')

        self.assertEqual(Item.objects.count(), 0)

    def test_status_code(self):
        list_ = List.objects.create()
        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)
        response = self.client.get(f'/core/lists/{list_.id}/items/{item.id}/item_edit')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        list_ = List.objects.create()
        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)
        response = self.client.get(f'/core/lists/{list_.id}/items/{item.id}/item_edit')
        self.assertTemplateUsed(response, 'apps/core/item_edit.html')

    def test_can_save_a_POST_request(self):
        list_ = List.objects.create()
        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)

        self.client.post(f'/core/lists/{list_.id}/items/{item.id}/item_edit',
                         data={'descricao': 'A new list item edited', 'cliente': 'Nalveira', 'valor_compra': '50',
                               'data_venda': str(date.today()), 'status': '0'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.descricao, 'A new list item edited')
        self.assertEqual(new_item.cliente, 'Nalveira')
        self.assertEqual(new_item.valor_compra, Decimal(50))
        self.assertEqual(new_item.data_venda, date.today())
        self.assertEqual(new_item.status, '0')

    def test_status_code(self):
        response = self.client.get(f'/core/precos/')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(f'/core/precos/')
        self.assertTemplateUsed(response, 'apps/core/precos.html')

    def test_uses_parcela_form(self):
        response = self.client.get(f'/core/precos/')
        self.assertIsInstance(response.context['form'], PrecoForm)

    def test_exists_ids_in_form_precos(self):
        form = PrecoForm()
        self.assertIn('id="id_preco"', form.as_p())


class ParcelaEditTest(TestCase):

    def test_status_code(self):
        list_ = List.objects.create()

        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)

        parcela = Parcela.objects.create(data_recebimento=date.today(), valor=Decimal(25), status='0', item=item)
        response = self.client.get(f'/core/lists/{list_.id}/items/{item.id}/parcelas/{parcela.id}/parcela_edit')
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        list_ = List.objects.create()

        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)

        parcela = Parcela.objects.create(data_recebimento=date.today(), valor=Decimal(25), status='0', item=item)
        response = self.client.get(f'/core/lists/{list_.id}/items/{item.id}/parcelas/{parcela.id}/parcela_edit')
        self.assertTemplateUsed(response, 'apps/core/parcela/parcela_edit.html')

    def test_can_save_a_POST_request(self):
        list_ = List.objects.create()

        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)

        parcela = Parcela.objects.create(data_recebimento=date.today(), valor=Decimal(25), status='0', item=item)

        self.client.post(f'/core/lists/{list_.id}/items/{item.id}/parcelas/{parcela.id}/parcela_edit',
                         data={'data_recebimento': str(date.today()), 'valor': '14', 'status': '0'})

        self.assertEqual(Parcela.objects.count(), 1)

        parcela = Parcela.objects.first()
        self.assertEqual(parcela.valor, Decimal(14))


class ParcelaDeleteTest(TestCase):

    # def test_status_code(self):
    #     list_ = List.objects.create()
    #
    #     item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
    #                                data_venda=date.today(), status='0', list=list_)
    #
    #     parcela = Parcela.objects.create(data_recebimento=date.today(), valor=Decimal(25), status='0', item=item)
    #
    #     response = self.client.get(f'/core/lists/{list_.pk}/items/{item.pk}/parcelas/{parcela.pk}/parcela_delete')
    #     self.assertEqual(response.status_code, 200)

    # def test_view_url_by_name(self):
    #     list_ = List.objects.create()
    #
    #     item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
    #                                data_venda=date.today(), status='0', list=list_)
    #
    #     parcela = Parcela.objects.create(data_recebimento=date.today(), valor=Decimal(25), status='0', item=item)
    #
    #     response = self.client.get(
    #         reverse('parcela_delete', kwargs={'list_pk': list_.pk, 'item_pk': item.pk, 'parcela_pk': parcela.pk}))
    #     self.assertEqual(response.status_code, 200)

    def test_delete(self):
        list_ = List.objects.create()

        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)

        parcela = Parcela.objects.create(data_recebimento=date.today(), valor=Decimal(25), status='0', item=item)

        self.client.post(
            reverse('parcela_delete', kwargs={'list_pk': list_.pk, 'item_pk': item.pk, 'parcela_pk': parcela.pk}))

        self.assertEqual(Parcela.objects.count(), 0)

    def test_redirects_after_POST(self):
        list_ = List.objects.create()

        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)

        parcela = Parcela.objects.create(data_recebimento=date.today(), valor=Decimal(25), status='0', item=item)

        response = self.client.post(
            reverse('parcela_delete', kwargs={'list_pk': list_.pk, 'item_pk': item.pk, 'parcela_pk': parcela.pk}))
        self.assertRedirects(response, reverse('item_detail', kwargs={'list_pk': list_.pk, 'item_pk': item.pk}))
