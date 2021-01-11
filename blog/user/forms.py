from django import forms
from django.forms import fields
from django.forms.widgets import PasswordInput

class RegisterForm (forms.Form):
    
    username= forms.CharField(max_length=100, label="User Name")
    password = forms.CharField(max_length=100,label="Password", widget=forms.PasswordInput)
    confirm= forms.CharField(max_length=50, label="Confirm", widget=forms.PasswordInput)
        
    def clean(self):
        username = self.cleaned_data.get("username")
        password =self.cleaned_data.get("password")
        confirm= self.cleaned_data.get("confirm")
        if confirm and password and password != confirm:
            raise forms.ValidationError("passwords do not match")
        
        values={
         'username': username,
         'password': password,
        }
        return values

class LoginForm (forms.Form):
    username= forms.CharField(label="User Name")
    password = forms.CharField(label="Password", widget=PasswordInput)