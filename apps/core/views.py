from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from apps.core.forms import ItemForm
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
