# Generated by Django 2.2.5 on 2019-11-12 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0024_auto_20191112_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Category'),
        ),
    ]
