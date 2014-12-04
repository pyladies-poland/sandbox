from django import forms
from django.views import generic
from accounts.models import *

class NewUserForm(generic.FormView):
    class Meta:
        model = User

