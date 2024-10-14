from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.models import User
from .models import Photo


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image','title', 'tag_category']

