from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #default arg is required = TRUE
    # name = forms.CharField()you can create a new field
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            # 'name',
            'email',
            'password1',
            'password2'
            ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']