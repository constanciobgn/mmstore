from django import forms

from apps.core.models import Item


class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = {'descricao', 'valor_compra', 'data_venda'}

    def save(self, for_list):
        self.instance.list = for_list
        return super().save()
