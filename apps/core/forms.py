from django import forms

from apps.core.models import Item, Parcela


class ItemForm(forms.models.ModelForm):
    field_order = ['descricao', 'valor_compra', 'data_venda', 'status']

    class Meta:
        model = Item
        fields = {'descricao', 'valor_compra', 'data_venda', 'status', }

    def save(self, for_list):
        self.instance.list = for_list
        return super().save()


class ParcelaForm(forms.models.ModelForm):
    field_order = ['data_recebimento', 'valor', 'status']

    class Meta:
        model = Parcela
        fields = {'data_recebimento', 'valor', 'status'}

    def save(self, for_item):
        self.instance.item = for_item
        return super().save()
