# Generated by Django 2.2.5 on 2019-11-06 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_remove_stock_no_of_copies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='purchase_detail',
        ),
    ]
