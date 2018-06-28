# Generated by Django 2.0.6 on 2018-06-28 13:07

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='valor_compra',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=5),
        ),
    ]
