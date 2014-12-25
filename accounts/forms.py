from django import forms

from accounts.models import User
from django.contrib.auth.forms import AuthenticationForm


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'surname', 'gender', 'telephone_number',
                  'address']
        widgets = {'password': forms.PasswordInput()}


class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {'password': forms.PasswordInput()}


class UserDataEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'gender', 'telephone_number', 'address', 'date_of_birth']


class UserPasswordChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']


class UserEmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']