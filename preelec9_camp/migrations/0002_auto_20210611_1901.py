# Generated by Django 3.2.3 on 2021-06-11 12:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('preelec9_camp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='add_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 11, 12, 1, 38, 790917, tzinfo=utc), null=True),
        ),
        migrations.AddField(
            model_name='statement',
            name='remarks',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='statement',
            name='division',
            field=models.CharField(choices=[('Art', 'Art'), ('Data', 'Data'), ('Delivery', 'Delivery'), ('Local', 'Local'), ('Medic', 'Medic'), ('PR', 'PR'), ('Recreation', 'Recreation'), ('Security', 'Security'), ('Secretary', 'Secretary'), ('Welfare', 'Welfare'), ('Treasurer', 'Treasurer'), ('Other', 'Other')], max_length=100),
        ),
    ]
