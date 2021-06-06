from django.db import models
from django.contrib.auth.models import User

class EEUserProfile(models.Model):
    gender_choices = [
        ('นาย', 'นาย'),
        ('นางสาว', 'นางสาว'),
    ]
    class Meta:
        db_table = 'auth_userprofile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=gender_choices, max_length=6, null=True)
    name = models.CharField(max_length=100,null=True)
    surname = models.CharField(max_length=100,null=True)
    nickname = models.CharField(max_length=30,null=True)
    student_id = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=1000, null=True)
    self_telephone_num = models.CharField(max_length=10, null=True)
    line_id = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name()
