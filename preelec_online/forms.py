from django import forms
from django.db.models import fields
from django.forms import widgets,Select,Textarea
from .models import Shop

class Shop_form(forms.Form):
    shop_choices = [
        ('powerbank', 'Powerbank'),
        ('bag', 'Bag'),
    ]
    division = forms.ChoiceField(
        choices = shop_choices, label = 'เลือกฝ่าย',
        widget=Select(attrs={'type': 'text','class': 'form-control'}
        ))

class Powerbank_form(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        exclude = ['user']
        widgets = {
                    'quantity_powerbank' : Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'จำนวน'}),
                    'color_powerbank' : Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'เลือกไซส์เสื้อ'},choices=Shop.powerbank_choices)
                    
    }

class Bag_form(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['__all__']
        widgets = {
                    'quantity_bag' : Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'จำนวน'}),
        }