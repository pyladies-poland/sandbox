from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from accounts.models import User
from accounts.forms import NewUserForm

class NewUserView(generic.FormView):
    template_name = "accounts/new_account.html"
    success_url = '/accounts/success/'
    form_class = NewUserForm