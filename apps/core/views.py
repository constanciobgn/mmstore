from django.http import HttpResponse
from django.shortcuts import render

from apps.core.forms import ItemForm


def hello_world(request):
    return HttpResponse('<h1>Hello World</h1>')


def mmstore_admin(request):
    form = ItemForm()
    return render(request, 'apps/core/index.html', {'form': form})

def new_list(request):
    pass