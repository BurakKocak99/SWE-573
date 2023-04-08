from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    Name_Surname = forms.CharField()

    class Meta:
        model = User
        fields = ["Name_Surname", "username", "email", "password1", "password2"]


