from datetime import date
from decimal import Decimal

from django.test import TestCase

from apps.core.forms import ItemForm, ParcelaForm
from apps.core.models import List, Item


class MMStoreAdminTest(TestCase):

    def test_exists_ids_in_form_item(self):
        form = ItemForm()
        self.assertIn('id="id_descricao"', form.as_p())
        self.assertIn('id="id_cliente"', form.as_p())
        self.assertIn('id="id_valor_compra"', form.as_p())
        self.assertIn('id="id_data_venda"', form.as_p())
        self.assertIn('id="id_status"', form.as_p())

    def test_uses_parcela_form(self):
        list_ = List.objects.create()
        item = Item.objects.create(descricao='The first list item', cliente='Nalveira', valor_compra=Decimal(50),
                                   data_venda=date.today(), status='0', list=list_)
        response = self.client.get(f'/core/lists/{list_.id}/items/{item.id}/add_parcela')
        self.assertIsInstance(response.context['form'], ParcelaForm)

    def test_exists_ids_in_form_parcela(self):
        form = ParcelaForm()
        self.assertIn('id="id_data_recebimento"', form.as_p())
        self.assertIn('id="id_valor"', form.as_p())
        self.assertIn('id="id_status"', form.as_p())
