# Generated by Django 3.2.3 on 2021-07-05 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preelec_online', '0007_auto_20210704_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]