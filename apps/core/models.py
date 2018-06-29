from datetime import date
from decimal import Decimal

from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
    descricao = models.CharField(default='', max_length=100)
    valor_compra = models.DecimalField(default=Decimal(0), decimal_places=2, max_digits=5)
    data_venda = models.DateField(default=date.today)
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
