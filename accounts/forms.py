from django import forms
from django.views import generic
from accounts.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User

