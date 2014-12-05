from django.views import generic
from django.contrib import messages

from accounts.forms import NewUserForm


class NewUserView(generic.CreateView):
    template_name = "accounts/new_account.html"
    success_url = '/accounts/success/'
    form_class = NewUserForm


    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Congratulation You Created a User profile!")
        return super(NewUserView, self).form_valid(form)
