# Generated by Django 2.2.5 on 2019-11-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20191105_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition_number',
            name='requisition_num',
            field=models.CharField(max_length=250),
        ),
    ]
