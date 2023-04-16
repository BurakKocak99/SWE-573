from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Story, Profile, CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

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
        model = CustomUser
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
    Biography = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "Username", "email", "Biography"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username",)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)