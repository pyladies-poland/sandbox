from django import forms

from accounts.models import User
from django.contrib.auth.forms import AuthenticationForm


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'surname', 'gender', 'telephone_number',
                  'address']
        widgets = {'password': forms.PasswordInput()}


class LogIn(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {'password': forms.PasswordInput()}