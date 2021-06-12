# Generated by Django 3.2.3 on 2021-06-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(choices=[('Art', 'Art'), ('Data', 'Data'), ('Delivery', 'Delivery'), ('Local', 'Local'), ('Medic', 'Medic'), ('PR', 'PR'), ('Recreation', 'Recreation'), ('Security', 'Security'), ('Secretary', 'Secretary'), ('Welfare', 'Welfare'), ('Treasurer', 'Treasurer')], max_length=100)),
                ('mode', models.CharField(choices=[('รายรับ', 'รายรับ'), ('รายจ่าย', 'รายจ่าย')], max_length=100)),
                ('transaction_date', models.DateField(null=True)),
                ('price', models.FloatField(null=True)),
                ('quantity', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Statement',
                'verbose_name_plural': 'Statements',
            },
        ),
    ]
