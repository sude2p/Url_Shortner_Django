from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
         # Set the password field widget to PasswordInput
        self.fields['password'].widget = forms.PasswordInput()