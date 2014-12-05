from django import forms
from django.contrib.auth.models import User

from accounts.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_email', 'user_password', 'user_name', 'user_surname', 'user_gender', 'user_telephone_number',
                  'user_address']


    widgets = {
        'user_password': forms.PasswordInput(),
    }

