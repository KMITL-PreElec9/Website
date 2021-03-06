from django.db import models
from django.contrib.auth.models import User

class EEUserProfile(models.Model):
    gender_choices = [
        ('นาย', 'นาย'),
        ('นางสาว', 'นางสาว'),
    ]
    religion_choices = [
        ('พุทธ', 'พุทธ'),
        ('คริสต์', 'คริสต์'),
        ('อิสลาม', 'อิสลาม'),
        ('อื่นๆ', 'อื่นๆ'),
    ]
    class Meta:
        db_table = 'auth_userprofile'
        verbose_name = "EEUserProfile"
        verbose_name_plural = "EEUserProfile"
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(choices=gender_choices, max_length=6, null=True)
    name = models.CharField(max_length=100,null=True)
    surname = models.CharField(max_length=100,null=True)
    eng_name = models.CharField(max_length=100,null=True)
    eng_surname = models.CharField(max_length=100,null=True)
    nickname = models.CharField(max_length=30,null=True)
    student_id = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=1000, null=True)
    self_telephone_num = models.CharField(max_length=10, null=True)
    line_id = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    religion = models.CharField(choices=religion_choices, max_length=6, null=True)
    allergic_foods = models.CharField(max_length=200, null=True)
    allergic_meds = models.CharField(max_length=200, null=True)
    congenital_disease =  models.CharField(max_length=100, null=True)
    completed = models.BooleanField(default= False)
    def __str__(self):
        return '{} {}'.format(self.name , self.surname)
    def updatename():
        db = EEUserProfile.objects.all()
        for obj in db:
            obj.eng_name = str(obj.user.first_name).title()
            obj.eng_surname = str(obj.user.last_name).title()
            obj.save()
        return True

class EEData(models.Model):
    class Meta:
        abstract = True
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100,null=True)
    student_id = models.IntegerField(null=True)
    self_telephone_num = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=200, null=True)
    email2 = models.EmailField(max_length=200, null=True)
    line_id = models.CharField(max_length=100, null=True)
    birth_date = models.DateField(null=True)
    nickname = models.CharField(max_length=30,null=True)
    used = models.BooleanField(default=False)
    def __str__(self):
        return '{} {}'.format(self.name , self.surname)

class EEData_63(EEData):
    class Meta:
        verbose_name = "EEData63"
        verbose_name_plural = "EEData63"

class EEData_64(EEData):
    class Meta:
        verbose_name = "EEData64"
        verbose_name_plural = "EEData64"

class EEData_62(EEData):
    class Meta:
        verbose_name = "EEData62"
        verbose_name_plural = "EEData62"

class EEData_61(EEData):
    class Meta:
        verbose_name = "EEData61"
        verbose_name_plural = "EEData61"

