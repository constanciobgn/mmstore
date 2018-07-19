# Generated by Django 2.0.6 on 2018-07-16 23:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_token_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='token',
            name='uid',
            field=models.CharField(default=uuid.uuid4, max_length=40),
        ),
    ]