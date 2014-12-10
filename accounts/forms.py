from django import forms

from accounts.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'surname', 'gender', 'telephone_number',
                  'address']
        widgets = {'password': forms.PasswordInput()}
