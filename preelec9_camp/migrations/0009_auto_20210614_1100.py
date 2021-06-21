# Generated by Django 3.2.3 on 2021-06-14 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preelec9_camp', '0008_remove_campdata_64_registered'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campdata_64',
            options={'verbose_name': 'Camp Data 64', 'verbose_name_plural': 'Camp Data 64'},
        ),
        migrations.AddField(
            model_name='campdata_64',
            name='registered_1_ts',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='campdata_64',
            name='registered_2_ts',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='campdata_64',
            name='registered_3_ts',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='campdata_64',
            name='registered_fin_ts',
            field=models.DateTimeField(null=True),
        ),
    ]