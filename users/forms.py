from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class edit_profile(forms.ModelForm):
    class Meta:
        model = profile
        fields = "__all__"


class AddStaffForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"
