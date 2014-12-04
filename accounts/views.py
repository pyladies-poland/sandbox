from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from accounts.models import User
from accounts.forms import NewUser

class NewUserForm(generic.FormView):
    template_name = "accounts/new_account.html"
    success_url = '/accounts/success/'
    form_class = User
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/accounts/success/')

        return render(request, self.template_name, {'form': form})