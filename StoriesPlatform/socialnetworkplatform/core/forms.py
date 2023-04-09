from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import User
from .models import Story,Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': ''
        }

    ))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    story = forms.CharField(widget=forms.Textarea())
    time = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'type': 'datetime-local'
        }
    ))
    placeID = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'hidden',
            'value': 'ChIJk6L3m5i6yhQRVJIzM4pE4A8',
            'id': 'placeID'
        }

    ))
    class Meta:
        model = Story
        fields = ["title", "story", "time", "placeID"]


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name","last_name", "Username", "email", "Biography"]