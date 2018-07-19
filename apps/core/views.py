from datetime import date

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from apps.core.forms import ItemForm, ParcelaForm, PrecoForm
from apps.core.models import List, Item, Parcela


def hello_world(request):
    return HttpResponse('<h1>Hello World</h1>')


def mmstore_admin(request):
    form = ItemForm()
    items = Item.objects.all()
    parcelas_atrasadas = Parcela.objects.filter(data_recebimento__lt=date.today(), status__exact='0')
    items_atrasados = Item.objects.filter(pk__in=parcelas_atrasadas.values_list('item_id', flat=True)).distinct()
    return render(request, 'apps/core/index.html',
                  {'form': form, 'items': items, 'items_atrasados': items_atrasados, })


def precos(request):
    form = PrecoForm(data=request.POST)

    if form.is_valid():
        item_price = form.cleaned_data['preco']

        sale_price_60 = item_price * 160 / 100
        sale_price_70 = item_price * 170 / 100
        sale_price_80 = item_price * 180 / 100
        sale_price_100 = item_price * 200 / 100

        return render(request, 'apps/core/precos.html', {'form': PrecoForm(),
                                                         'sale_price_60': [sale_price_60,
                                                                           sale_price_60 - item_price],
                                                         'sale_price_70': [sale_price_70,
                                                                           sale_price_70 - item_price],
                                                         'sale_price_80': [sale_price_80,
                                                                           sale_price_80 - item_price],
                                                         'sale_price_100': [sale_price_100,
                                                                            sale_price_100 - item_price]
                                                         })
    return render(request, 'apps/core/precos.html', {'form': form})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(reverse('mmstore_admin'))
    return render(request, 'apps/core/index.html', {'form': form})


def add_parcela(request, list_pk, item_pk):
    form = ParcelaForm(data=request.POST)
    item = Item.objects.get(id=item_pk)
    if request.method == 'POST':
        if form.is_valid():
            form.save(for_item=item)
            return redirect(f'/core/lists/0/items/{item.id}/add_parcela')
    return render(request, 'apps/core/parcela/new.html', {'form': form, 'item': item, })


def item_detail(request, list_pk, item_pk):
    item = Item.objects.get(id=item_pk)
    return render(request, 'apps/core/item_detail.html', {'item': item, })


def item_delete(request, list_pk, item_pk):
    item = Item.objects.get(id=item_pk)
    item.delete()
    return redirect(reverse('mmstore_admin'))


def item_edit(request, list_pk, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    form = ItemForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            Item.objects.filter(id=item_pk).update(descricao=form.cleaned_data['descricao'],
                                                   cliente=form.cleaned_data['cliente'],
                                                   valor_compra=form.cleaned_data['valor_compra'],
                                                   data_venda=form.cleaned_data['data_venda'],
                                                   status=form.cleaned_data['status'])
            return redirect(reverse('mmstore_admin'))
    return render(request, 'apps/core/item_edit.html', {'form': form, 'item': item, })


def parcela_delete(request, list_pk, item_pk, parcela_pk):
    parcela = Parcela.objects.get(id=parcela_pk)
    parcela.delete()
    return redirect(reverse('item_detail', kwargs={'list_pk': list_pk, 'item_pk': item_pk}))


def parcela_edit(request, list_pk, item_pk, parcela_pk):
    parcela = get_object_or_404(Parcela, pk=parcela_pk)
    item = get_object_or_404(Item, pk=item_pk)
    form = ParcelaForm(data=request.POST or None, instance=parcela)
    if request.method == 'POST':
        if form.is_valid():
            Parcela.objects.filter(id=parcela_pk).update(data_recebimento=form.cleaned_data['data_recebimento'],
                                                         valor=form.cleaned_data['valor'],
                                                         status=form.cleaned_data['status'])
            return redirect(reverse('item_detail', kwargs={'list_pk': list_pk, 'item_pk': item_pk}))
    return render(request, 'apps/core/parcela/parcela_edit.html', {'form': form, 'item': item, 'parcela': parcela})
