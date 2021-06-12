# Generated by Django 3.2.3 on 2021-06-10 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_auth', '0002_auto_20210606_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='EEData_63',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_id', models.IntegerField(null=True)),
                ('self_telephone_num', models.CharField(max_length=9, null=True)),
                ('line_id', models.CharField(max_length=100, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('nickname', models.CharField(max_length=30, null=True)),
                ('used', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='eeuserprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='eeuserprofile',
            name='self_telephone_num',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='eeuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='EEData_64',
            fields=[
                ('eedata_63_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='site_auth.eedata_63')),
            ],
            bases=('site_auth.eedata_63',),
        ),
    ]
