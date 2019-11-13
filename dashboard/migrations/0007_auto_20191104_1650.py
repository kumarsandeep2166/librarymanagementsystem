# Generated by Django 2.2.5 on 2019-11-04 11:20

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20191102_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=dashboard.models.PathAndRename('attachment/2019/11/04')),
        ),
        migrations.AlterField(
            model_name='profile',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=dashboard.models.PathAndRename('logo/2019/11/04')),
        ),
        migrations.AlterField(
            model_name='profile',
            name='other_attachment',
            field=models.FileField(blank=True, null=True, upload_to=dashboard.models.PathAndRename('attachment/2019/11/04')),
        ),
    ]
