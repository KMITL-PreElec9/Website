from django import forms
from django.forms import widgets
from .models import Campdata_64
class RegisterForm_64(forms.ModelForm):
    class Meta:
        model = Campdata_64
        fields = '__all__'
        exclude = ['user']
        #widgets = {}
