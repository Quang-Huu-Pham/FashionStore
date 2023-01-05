from django import forms
# import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
