from datetime import tzinfo
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.
class Camp_online_6x(models.Model):
    class Meta:
        verbose_name = "Camp_online_6x" 
        verbose_name_plural = "Camp_online_6x"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    price= models.IntegerField(null= True)
    check_shop = models.ImageField('หลักฐานการโอน',upload_to='images/preelec_online/shop',null=True)    
    completed = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)

class Camp_online_64(models.Model):
    class Meta:
        verbose_name = "Camp_online_64"
        verbose_name_plural = "Camp_online_64"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)
    
class Shop(models.Model):
    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shop"
    shop_choices = [
        ('Powerbank', 'Powerbank'),
        ('Bag', 'Bag')
    ]
    camp_online_6x = models.ForeignKey(Camp_online_6x, on_delete=models.CASCADE,null=True)
    color = models.CharField(max_length=100,null = True)
    quantity = models.IntegerField()
    shop_choices = models.CharField(max_length=100, choices = shop_choices)
    price = models.IntegerField(null = True)
    def __str__(self):
        return str(self.camp_online_6x)
    def save(self, user ,*args, **kwargs):
        if not hasattr(user, 'camp_online_6x'):
            db = Camp_online_6x(user = user)
            db.save()
        else: db = user.camp_online_6x
        self.camp_online_6x = db
        return super().save()
class Activity_Camp(models.Model):
    class Meta:
        verbose_name = "Activity_Camp"
        verbose_name_plural = "Activity_Camp"
    activity_name = models.CharField(max_length=100, null=True)
    activity_date = models.DateField(null=True)
    activity_beginning_time = models.TimeField(null=True)
    activity_end_time = models.TimeField(null=True)
    activity_description = models.CharField(max_length=100, null=True)
    activity_caretaker = models.CharField(max_length=100, null=True)
    activity_place = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.activity_name)
    def get_date_headers():
        db = Activity_Camp.objects.all().values().order_by('activity_date')
        headers = []
        for element in db:
            if not element['activity_date'] in headers:
                headers.append(element['activity_date'])
        return headers
    def get_data_by_headers(headers):
        db = Activity_Camp.objects.all().values()
        data = []
        for header in headers:
            data_dict = db.filter(activity_date = header).order_by('activity_beginning_time')
            for element in data_dict:
                element['is_active'] = False
                date = datetime.now().date()
                time = datetime.now().time()
                starttime = element['activity_beginning_time']
                endtime = element['activity_end_time']
                if element['activity_date'] == date :
                    if starttime < time  <endtime:
                        element['is_active'] = True
            data.append(data_dict)
        return data

