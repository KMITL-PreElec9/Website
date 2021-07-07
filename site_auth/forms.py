from allauth.account.forms import LoginForm,SignupForm,ChangePasswordForm,ResetPasswordForm,AddEmailForm
from django import forms
from django.forms import fields,DateInput,Select,Textarea, widgets

from .models import EEUserProfile

class EELoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(EELoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder':'ชื่อผู้ใช้'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'รหัสผ่าน'})

class EESignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(EESignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder':'ชื่อผู้ใช้'})
        self.fields['email'].widget = forms.TextInput(attrs={'type': 'email','class': 'form-control', 'placeholder':'อีเมล'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder':'รหัสผ่าน'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder':'ยืนยันรหัสผ่าน'})

class EEChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(EEChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['oldpassword'].widget = forms.PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder':'รหัสผ่านปัจจุบัน'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder':'รหัสผ่านใหม่'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder':'ยืนยันรหัสผ่านใหม่'})

class EEResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(EEResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'type': 'email','class': 'form-control', 'placeholder':'อีเมล'})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = EEUserProfile
        fields = '__all__'
        exclude = ['user', 'completed']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget = Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'เพศ'},choices=EEUserProfile.gender_choices)
        self.fields['name'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'ชื่อ'})
        self.fields['surname'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'นามสกุล'})
        self.fields['eng_name'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'ชื่อ (ภาษาอังกฤษ)'})
        self.fields['eng_surname'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'นามสกุล (ภาษาอังกฤษ)'})
        self.fields['nickname'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'ชื่อเล่น'})
        self.fields['student_id'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'รหัสนักศึกษา'})
        self.fields['birth_date'].widget = DateInput(attrs={'type': 'date'})
        self.fields['address'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'ที่อยู่'})
        self.fields['self_telephone_num'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'เบอร์โทรศัพท์ส่วนตัว'})
        self.fields['line_id'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'Line id'})
        self.fields['facebook'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'Facebook'})
        self.fields['instagram'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'instagram '})
        self.fields['religion'].widget = Select(attrs={'type': 'text','class': 'form-control', 'placeholder':'ศาสนา'},choices=EEUserProfile.religion_choices)
        self.fields['allergic_foods'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'อาหารที่แพ้'})
        self.fields['allergic_meds'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'ยาที่แพ้ '})
        self.fields['congenital_disease'].widget = forms.TextInput(attrs={'type': 'text','class': 'form-control', 'placeholder':'โรคประจำตัว '})


class EEAddEmailForm(AddEmailForm):
    def __init__(self, *args, **kwargs):
        super(EEAddEmailForm, self).__init__(*args, **kwargs)
        
        self.fields['email'].widget = forms.TextInput(attrs={'type': 'email','class': 'form-control', 'placeholder':'อีเมล'})
