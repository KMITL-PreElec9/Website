# Generated by Django 3.2.3 on 2021-07-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preelec_online', '0009_auto_20210705_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp_online_6x',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
