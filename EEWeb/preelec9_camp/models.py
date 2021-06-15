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
    def get_data_by_division(self, division, *args, **kwargs):
        data1 = self.objects.filter(division = division, mode = 'รายรับ').values()
        data2 = self.objects.filter(division = division, mode = 'รายจ่าย').values()
        result = []; total1 = 0; total2 =0
        def add_data_to_template(*args, **kwargs):
            data_template = {
                'transaction_date' : args[0].strftime('%Y-%m-%d'),
                'name' : args[1], 'quantity' : args[2],
                'price' : args[3], 'income' : args[4],
                'expenditure' : args[5], 'remarks' : args[6]
            }
            return data_template
        def sort_key(d):
            return d['transaction_date']
        for i in range(len(data1)):
            st = data1[i]['price']*data1[i]['quantity']
            total1 = total1 + st
            result.append(add_data_to_template(
                data1[i]['transaction_date'], data1[i]['item_name'],
                data1[i]['quantity'], data1[i]['price'], st, '-', 
                data1[i]['remarks']
            ))
        for i in range(len(data2)):
            st = data2[i]['price']*data2[i]['quantity']
            total2 = total2 - st
            result.append(add_data_to_template(
                data2[i]['transaction_date'], data2[i]['item_name'],
                data2[i]['quantity'], data2[i]['price'], '-', st,
                data2[i]['remarks']
            ))
        result.sort(key = sort_key)
        return result, total1,total2
          
    def __str__(self):
        return str(self.item_name)
    
class Campdata_64(models.Model):
    class Meta:
        verbose_name = "Camp Data 64"
        verbose_name_plural = "Camp Data 64"
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
    #registered = models.BooleanField(default=False)
    house = models.CharField(max_length=2, choices = house_choices, null=True)
    def __str__(self):
        return str(self.user)
class Camp_Registered_64(models.Model):
    class Meta:
        verbose_name = "Camp Registered 64"
        verbose_name_plural = "Camp Registered 64"
    campdata_64 = models.ForeignKey(Campdata_64, on_delete=models.CASCADE)
    registered_on_1 = models.DateTimeField(null= True)
    registered_on_2 = models.DateTimeField(null= True)
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300, null=True)

