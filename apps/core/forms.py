from django import forms

from apps.core.models import Item, Parcela


class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = {'descricao', 'valor_compra', 'data_venda'}

    def save(self, for_list):
        self.instance.list = for_list
        return super().save()


class ParcelaForm(forms.models.ModelForm):
    class Meta:
        model = Parcela
        fields = {'data_recebimento', 'valor'}

    def save(self, for_item):
        self.instance.item = for_item
        return super().save()
