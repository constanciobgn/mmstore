# Generated by Django 2.0.6 on 2018-07-16 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_token_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='uid',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
