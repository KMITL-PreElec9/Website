from allauth.account.forms import LoginForm,SignupForm
from django import forms

class EELoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(EELoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder':'ชื่อผู้ใช้'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'รหัสผ่าน'})

class EESignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(EESignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder':'ชื่อผู้ใช้'})
        self.fields['email'].widget = forms.PasswordInput(attrs={'type': 'email','class': 'form-control', 'placeholder':'อีเมล'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder':'รหัสผ่าน'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder':'ยืนยันรหัสผ่าน'})