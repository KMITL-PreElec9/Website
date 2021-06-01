from allauth.account.forms import LoginForm
from django import forms

class EELoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(EELoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder':'ชื่อผู้ใช้'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'รหัสผ่าน'})