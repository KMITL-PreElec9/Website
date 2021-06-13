from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Statement(models.Model):
    class Meta:
        verbose_name = "Statement"
        verbose_name_plural = "Statements"
    division_choices = [
        ('Art', 'Art'),
        ('Data', 'Data'),
        ('Delivery', 'Delivery'),
        ('Local', 'Local'),
        ('Medic', 'Medic'),
        ('PR', 'PR'),
        ('Recreation', 'Recreation'),
        ('Security', 'Security'),
        ('Secretary', 'Secretary'),
        ('Welfare', 'Welfare'),
        ('Treasurer', 'Treasurer'),
        ('Other', 'Other')
    ]
    mode_choices = [
        ('รายรับ', 'รายรับ'),
        ('รายจ่าย', 'รายจ่าย'),
    ]
    division = models.CharField(max_length=100, choices=division_choices)
    mode = models.CharField(max_length=100, choices = mode_choices)
    item_name = models.CharField(max_length=300, default='')
    transaction_date = models.DateField(null=True)
    add_date = models.DateField(null=True, default= timezone.now)
    price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    remarks = models.CharField(max_length=1000, null= True)

    def __str__(self):
        return self.item_name
    
class Campdata_64(models.Model):
    class Meta:
        verbose_name = "CampData64"
        verbose_name_plural = "CampData64"
    shirt_size_choices = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]
    house_choices = [
        ('AR', 'Ares'),
        ('PO', 'Poseidon'),
        ('ZE', 'Zeus'),
        ('HE', 'Hermes'),
    ]
    parent_gender_choices = [
        ('นาย', 'นาย'),
        ('นาง', 'นาง'),
        ('นางสาว', 'นางสาว'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    shirt_size = models.CharField(max_length=100, choices = shirt_size_choices)
    passion = models.CharField(max_length=1000, null= True)
    parent_telephone_num = models.CharField(max_length=10, null= True)
    parent_gender=models.CharField(max_length=10, null= True, choices=parent_gender_choices)
    parent_name = models.CharField(max_length=100, null= True)
    parent_surname = models.CharField(max_length=100, null= True)
    parent_relation = models.CharField(max_length=100, null= True)
    completed = models.BooleanField(default=False)
    registered = models.BooleanField(default=False)
    house = models.CharField(max_length=2, choices = house_choices, null=True)
    def __str__(self):
        return self.user