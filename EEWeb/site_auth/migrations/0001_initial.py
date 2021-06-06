# Generated by Django 3.2.3 on 2021-06-03 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EEUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('นาย', 'นาย'), ('นางสาว', 'นางสาว')], max_length=6, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('surname', models.CharField(max_length=100, null=True)),
                ('nickname', models.CharField(max_length=30, null=True)),
                ('student_id', models.IntegerField(null=True)),
                ('birth_date', models.DateField(null=True)),
                ('address', models.CharField(max_length=1000, null=True)),
                ('self_telephone_num', models.CharField(max_length=10, null=True)),
                ('line_id', models.CharField(max_length=100, null=True)),
                ('facebook', models.CharField(max_length=100, null=True)),
                ('instagram', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auth_userprofile',
            },
        ),
    ]