# Generated by Django 3.2.3 on 2021-06-30 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('preelec9_camp', '0018_auto_20210624_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campdata_6x',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_shirt', models.ImageField(null=True, upload_to='images/preelec9_camp/shirt', verbose_name='หลักฐานการโอน')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Camp Data 6x',
                'verbose_name_plural': 'Camp Data 6x',
            },
        ),
    ]
