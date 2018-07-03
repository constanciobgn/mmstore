from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from apps.core.forms import ItemForm, ParcelaForm
from apps.core.models import List, Item


def hello_world(request):
    return HttpResponse('<h1>Hello World</h1>')


def mmstore_admin(request):
    form = ItemForm()
    items = Item.objects.all()
    return render(request, 'apps/core/index.html', {'form': form, 'items': items})


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
