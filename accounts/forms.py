from django import forms

from accounts.models import User
from django.contrib.auth.forms import AuthenticationForm


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'surname', 'gender', 'telephone_number',
                  'address']
        widgets = {'password': forms.PasswordInput()}


class LogInForm(forms.Form):
    email = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())
    widgets = {'password': forms.PasswordInput()}


class UserDataEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'gender', 'telephone_number', 'address', 'date_of_birth']


class UserPasswordChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']

    new_password_1 = forms.CharField(max_length=30, min_length=8)
    new_password_2 = forms.CharField(max_length=30, min_length=8)

class UserEmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']