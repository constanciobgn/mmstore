from datetime import date
from decimal import Decimal

from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
    descricao = models.CharField(default='', max_length=100)
    cliente = models.CharField(default='', max_length=100)
    valor_compra = models.DecimalField(default=Decimal(0), decimal_places=2, max_digits=5)
    data_venda = models.DateField(default=date.today)
    STATUS_CHOICES = (('0', 'Recebendo'), ('1', 'Finalizado'),)
    status = models.CharField(default='0', choices=STATUS_CHOICES, max_length=1)
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-data_venda',)


class Parcela(models.Model):
    data_recebimento = models.DateField(default=date.today)
    valor = models.DecimalField(default=Decimal(0), decimal_places=2, max_digits=5)
    STATUS_CHOICES = (('0', 'Pendente'), ('1', 'Pago'),)
    status = models.CharField(default='0', choices=STATUS_CHOICES, max_length=1)
    item = models.ForeignKey(Item, default=None, on_delete=models.CASCADE)

    class Meta:
        ordering = ('data_recebimento',)
