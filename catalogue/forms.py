from django import forms
from django.forms import ModelForm, modelform_factory
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from pkg_resources import require
from .models import RATE_CHOICES, Profile, Review

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment','rate']

class UserUpdateForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']