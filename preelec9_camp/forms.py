from django import forms
from django.db.models import fields
from django.forms import widgets,Select,Textarea
from .models import Campdata_64, Statement,Shirt,Campdata_63
class RegisterForm_64(forms.ModelForm):
    class Meta:
        model = Campdata_64
        fields = '__all__'
        exclude = ['user', 'completed', 'registered', 'house']
        widgets = {'shirt_size' : Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'เลือกไซส์เสื้อ'},choices=Campdata_64.shirt_size_choices),
                    'parent_gender' : Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'เลือกไซส์เสื้อ'},choices=Campdata_64.parent_gender_choices),
                    'passion' : forms.Textarea(attrs={'type': 'text','class': 'form-control', 'placeholder':'มีอะไรจะบอกพี่ๆ, ทำไมถึงเข้าที่นี่, สิ่งที่คาดหวังจากที่นี่'}),
                    'parent_telephone_num' : forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'เบอร์ติดต่อผู้ปกครอง'}),
                    'parent_name': forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'ชื่อผู้ปกครอง'}),
                    'parent_surname': forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'นามสกุลผู้ปกครอง'}),
                    'parent_relation': forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'บิดา, มารดา , .....'})
        
        }
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
        ('Welcome Box','Welcome Box'),
        ('Other', 'Other'),
    ]
    division = forms.ChoiceField(
        choices = division_choices, label = 'เลือกฝ่าย',
        widget=Select(attrs={'type': 'text','class': 'form-control'}
        ))

class RegisterForm_63(forms.ModelForm):
    class Meta:
        model = Shirt
        fields = '__all__'
        exclude = ['user']
        widgets = {'size_shirt' : Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'เลือกไซส์เสื้อ'},choices=Shirt.shirt_size_choices),
                    'quantity_shirt' : Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'เลือกไซส์เสื้อ'},choices=Shirt.shirt_quantity_choices),
                    'color_shirt' : Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'เลือกไซส์เสื้อ'},choices=Shirt.shirt_color_choices)
                    
    }

class Check_shirtForm(forms.ModelForm):
    class Meta:
        model = Campdata_63
        fields = ['check_shirt']
        