from django import forms
from django.forms import widgets,Select,Textarea
from .models import Campdata_64
class RegisterForm_64(forms.ModelForm):
    class Meta:
        model = Campdata_64
        fields = '__all__'
        exclude = ['user', 'completed', 'registered', 'house']
        widgets = {'shirt_size' : Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'เลือกไซส์เสื้อ'},choices=Campdata_64.shirt_size_choices),
                    'passion' : forms.Textarea(attrs={'type': 'text','class': 'form-control', 'placeholder':'มีอะไรจะบอกพี่ๆ, ทำไมถึงเข้าที่นี่, สิ่งที่คาดหวังจากที่นี่'}),
                    'parent_telephone_num' : forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'เบอร์ติดต่อผู้ปกครอง'}),
                    'parent_name': forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'ชื่อผู้ปกครอง'})
        }
