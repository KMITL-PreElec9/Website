from allauth.account.forms import LoginForm,SignupForm,ChangePasswordForm,ResetPasswordForm
from django import forms
from django.forms import fields
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
        self.fields['email'].widget = forms.PasswordInput(attrs={'type': 'email','class': 'form-control', 'placeholder':'อีเมล'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder':'รหัสผ่าน'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder':'ยืนยันรหัสผ่าน'})

class EEChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(EEChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder':'รหัสผ่านปัจจุบัน'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder':'รหัสผ่านใหม่'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'type': 'password','class': 'form-control', 'placeholder':'ยืนยันรหัสผ่านใหม่'})

class EEResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(EEResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.PasswordInput(attrs={'type': 'email','class': 'form-control', 'placeholder':'อีเมล'})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = EEUserProfile
        fields = [
            'gender', 'name', 'surname', 'nickname',
            'student_id', 'birth_date', 'address', 'self_telephone_num',
            'line_id', 'facebook', 'instagram'
            ]
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['birth_date'].widget = forms.DateInput(attrs={'type': 'date'})
        
