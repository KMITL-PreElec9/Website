from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets,Select,Textarea
from .models import Camp_online_6x, Shop

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
        img_url = 'https://s.isanook.com/ca/0/ui/279/1396205/download20190701165129_1562561119.jpg'
        display_name = 'Powerbank'
        form_name = 'powerbank'
        model = Shop
        fields=['quantity','color']
        powerbank_choices = [
            ('white', 'White'),
            ('black', 'Black')
        ]
        quantity_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ]
        widgets = {
                    'quantity' : Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'จำนวน'},choices=quantity_choices),
                    'color' : Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'เลือกไซส์เสื้อ'},choices=powerbank_choices)
                    
    }
    def save(self, user, *args, **kwargs):
        model = super().save(commit= False)
        model.shop_choices = 'powerbank'
        model.price = 300
        model.save(user = user)
        return model


class Bag_form(forms.ModelForm):
    class Meta:
        img_url = 'http://i1.wp.com/poshmagazinethailand.com/wp-content/uploads/2017/08/The-Ten_Air-Jordan-I-x-Virgil-Abloh.jpg?fit=1800%2C2240'
        display_name = 'ถุงผ้า'
        form_name = 'bag'
        model = Shop
        fields = ['quantity']
        quantity_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ]
        widgets = {
                    'quantity' : Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'จำนวน'},choices=quantity_choices),
        }
    def save(self, user, *args, **kwargs):
        model = super().save(commit= False)
        model.shop_choices = 'bag'
        model.price = 150
        model.color = 'white'
        model.save(user = user)
        return model

class ShopCheckoutForm(forms.ModelForm):
    class Meta:
        model = Camp_online_6x
        fields = ['check_shop']
    def save(self, commit: bool):
        model = super().save(commit=False)
        model.completed = True
        if commit == True:
            model.save()
        return model

