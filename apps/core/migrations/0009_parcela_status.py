# Generated by Django 2.0.6 on 2018-06-29 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_item_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcela',
            name='status',
            field=models.CharField(choices=[('0', 'Pendente'), ('1', 'Pago')], default='0', max_length=1),
        ),
    ]