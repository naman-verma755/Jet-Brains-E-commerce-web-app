# Generated by Django 3.1.3 on 2020-11-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20201118_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='keyword',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
