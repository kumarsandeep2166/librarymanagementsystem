# Generated by Django 2.2.5 on 2019-11-06 05:58

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20191105_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=dashboard.models.PathAndRename('attachment/2019/11/06')),
        ),
        migrations.AlterField(
            model_name='profile',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=dashboard.models.PathAndRename('logo/2019/11/06')),
        ),
        migrations.AlterField(
            model_name='profile',
            name='other_attachment',
            field=models.FileField(blank=True, null=True, upload_to=dashboard.models.PathAndRename('attachment/2019/11/06')),
        ),
    ]
