# Generated by Django 2.2.5 on 2019-11-11 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20191111_1206'),
        ('library', '0020_auto_20191107_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookIssueReturnStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField()),
                ('return_date', models.DateField()),
                ('expected_return_date', models.DateField()),
                ('fine_collected_date', models.DateField()),
                ('status', models.CharField(choices=[('available', 'available'), ('not available', 'not available')], max_length=50)),
                ('fine_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('book_accn_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Stock')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.DeleteModel(
            name='BookIssue',
        ),
    ]
