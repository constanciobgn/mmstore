# Generated by Django 2.0.6 on 2018-06-29 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_parcela'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('0', 'Recebendo'), ('1', 'Finalizado')], default='0', max_length=1),
        ),
    ]
