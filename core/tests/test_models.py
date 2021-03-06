from datetime import date
from decimal import Decimal

from django.test import TestCase

from core.models import List, Item, Parcela


class ListTest(TestCase):

    def test_saving_and_retrieving(self):
        list_ = List.objects.create()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)


class ItemTest(TestCase):

    def test_saving_and_retrieving(self):
        list_ = List.objects.create()

        Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                            data_venda=date.today(), status='0', list=list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 1)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.descricao, 'The first list item')
        self.assertEqual(first_saved_item.cliente, 'Nalveira')
        self.assertEqual(first_saved_item.valor_compra, Decimal(50))
        self.assertEqual(first_saved_item.valor_venda, Decimal(0))
        self.assertEqual(first_saved_item.data_venda, date.today())
        self.assertEqual(first_saved_item.status, '0')
        self.assertEqual(first_saved_item.list, list_)


class ParcelaTest(TestCase):

    def test_saving_and_retrieving(self):
        list_ = List.objects.create()

        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)

        Parcela.objects.create(data_recebimento=date.today(), valor=Decimal(25), status='0', item=item)

        saved_parcelas = Parcela.objects.all()
        self.assertEqual(saved_parcelas.count(), 1)

        first_saved_parcela = saved_parcelas[0]
        self.assertEqual(first_saved_parcela.data_recebimento, date.today())
        self.assertEqual(first_saved_parcela.valor, Decimal(25))
        self.assertEqual(first_saved_parcela.status, '0')

