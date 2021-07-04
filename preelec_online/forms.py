from django import forms
from django.db import models
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
        display_name = 'สั่ง Powerbank'
        form_name = 'powerbank'
        model = Shop
        fields=['quantity','color']
        powerbank_choices = [
            ('white', 'White'),
            ('black', 'Black')
        ]
        widgets = {
                    'quantity' : forms.NumberInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'จำนวน'}),
                    'color' : Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'เลือกไซส์เสื้อ'},choices=powerbank_choices)
                    
    }
    def save(self, user, *args, **kwargs):
        model = super().save(commit= False)
        model.shop_choices = 'powerbank'
        model.save(user = user)
        return model


class Bag_form(forms.ModelForm):
    class Meta:
        display_name = 'สั่งถุงผ้า'
        form_name = 'bag'
        model = Shop
        fields = ['quantity']
        widgets = {
                    'quantity' : forms.NumberInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'จำนวน'}),
        }
    def save(self, user, *args, **kwargs):
        model = super().save(commit= False)
        model.user = user
        model.shop_choices = 'bag'
        model.save(user = user)
        return model