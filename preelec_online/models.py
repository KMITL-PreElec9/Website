from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Camp_online_6x(models.Model):
    class Meta:
        verbose_name = "Camp_online_6x"
        verbose_name_plural = "Camp_online_6x"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    check_shop = models.ImageField('หลักฐานการโอน',upload_to='images/preelec_online/shop',null=True)    
    completed = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)

class Camp_online_64(models.Model):
    class Meta:
        verbose_name = "Camp_online_64"
        verbose_name_plural = "Camp_online_64"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
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
