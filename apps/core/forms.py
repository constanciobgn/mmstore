from django import forms


class ItemForm(forms.Form):
    descricao = forms.CharField()
    valor_compra = forms.DecimalField()