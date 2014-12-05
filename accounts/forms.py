from django import forms

from accounts.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User

    widgets = {
        'user_password': forms.PasswordInput(),
    }

