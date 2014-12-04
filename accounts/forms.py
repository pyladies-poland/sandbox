from django import forms
from accounts.models import *

class NewUser(forms.ModelForm):
    class Meta:
        model = User

