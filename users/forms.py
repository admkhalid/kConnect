from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #default arg is required = TRUE
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'second_name',
            'email',
            'password1',
            'password2'
            ]