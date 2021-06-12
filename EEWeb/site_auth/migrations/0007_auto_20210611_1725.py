# Generated by Django 3.2.3 on 2021-06-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_auth', '0006_auto_20210611_1722'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EEData_64',
        ),
        migrations.CreateModel(
            name='EEData_64',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100, null=True)),
                ('student_id', models.IntegerField(null=True)),
                ('self_telephone_num', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('line_id', models.CharField(max_length=100, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('nickname', models.CharField(max_length=30, null=True)),
                ('used', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'EEData64',
                'verbose_name_plural': 'EEData64',
            },
        ),
    ]
