# Generated by Django 2.2.5 on 2019-10-31 10:34

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20191029_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=dashboard.models.PathAndRename('attachment/2019/10/31')),
        ),
        migrations.AlterField(
            model_name='profile',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=dashboard.models.PathAndRename('logo/2019/10/31')),
        ),
        migrations.AlterField(
            model_name='profile',
            name='other_attachment',
            field=models.FileField(blank=True, null=True, upload_to=dashboard.models.PathAndRename('attachment/2019/10/31')),
        ),
    ]
