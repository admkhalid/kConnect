from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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