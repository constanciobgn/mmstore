"""mmstore_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.core.views import hello_world, mmstore_admin, new_list, add_parcela, item_detail, item_delete

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', hello_world, name='hello_world'),

    path('core/', mmstore_admin, name='mmstore_admin'),
    path('core/lists/new', new_list, name='new_list'),
    path('core/lists/<int:list_pk>/items/<int:item_pk>', item_detail, name='item_detail'),
    path('core/lists/<int:list_pk>/items/<int:item_pk>/add_parcela', add_parcela, name='add_parcela'),
    path('core/lists/<int:list_pk>/items/<int:item_pk>/item_delete', item_delete, name='item_delete'),
]
