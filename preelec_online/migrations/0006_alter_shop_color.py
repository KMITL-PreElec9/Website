# Generated by Django 3.2.3 on 2021-07-04 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preelec_online', '0005_auto_20210704_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='color',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
