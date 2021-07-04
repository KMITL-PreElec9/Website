from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Camp_online_6x(models.Model):
    class Meta:
        verbose_name = "Camp_online_6x"
        verbose_name_plural = "Camp_online_6x"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    check_shop = models.ImageField('หลักฐานการโอน',upload_to='images/preelec_online/shop',null=True)
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
        verbose_name = "Size_shirt"
        verbose_name_plural = "Size_shirt"
    shop_choices = [
        ('powerbank', 'Powerbank'),
        ('bag', 'Bag')
    ]
    powerbank_choices = [
        ('white', 'White'),
        ('black', 'Black')
    ]
    camp_online_6x = models.ForeignKey(Camp_online_6x, on_delete=models.CASCADE,null=True)
    powerbank_color = models.CharField(max_length=100, choices = powerbank_choices,null=True)
    quantity = models.IntegerField()
    shop_choices = models.CharField(max_length=100, choices = shop_choices)
    def __str__(self):
        return str(self.user)

