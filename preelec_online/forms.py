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
        img_url = "assets/img/power_bank.png"
        display_name = 'Powerbank'
        form_name = 'powerbank'
        price = 389
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
        model.price = 389
        model.save(user = user)
        return model


class Bag_form(forms.ModelForm):
    class Meta:
        img_url = "assets/img/bag.png"
        display_name = 'ถุงผ้า'
        form_name = 'bag'
        price = 139
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
        model.price = 139
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

class StatementForm_63(forms.Form):
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
        ('Other', 'Other'),
        ('All', 'All')
    ]
    division = forms.ChoiceField(
        choices = division_choices, label = 'เลือกฝ่าย',
        widget=Select(attrs={'type': 'text','class': 'form-control'}
        ))

