import datetime, random, sha

from django.views import generic
from django.contrib import messages
from django.core.mail import send_mail

from accounts.forms import NewUserForm
from sandbox.settings import EMAIL_HOST_USER


class NewUserView(generic.CreateView):
    template_name = "accounts/new_account.html"
    success_url = '/accounts/success/'
    form_class = NewUserForm


    def form_valid(self, form):
        new_user = form.save()
        new_user.save()
        salt = sha.new(str(random.random())).hexdigest()[:5]
        new_user.user_activation_key = sha.new(salt+new_user.username).hexdigest()
        new_user.user_akey_expires = datetime.datetime.today() + datetime.timedelta(2)
        new_user.save()
        subject = "SandboxApp: Confirm registration"
        text = "Hi %s, \n please confirm Your registration by clicking or copy-past this link \n __link__ \n Thank " \
               "You for using our app. \n Your Sandbox Team" %new_user.user_name
        send_mail(subject, text, EMAIL_HOST_USER, [new_user.user_email], fail_silently=False)

        messages.success(self.request, "Congratulation You Created a User profile! Please check Your e-mail")
        return super(NewUserView, self).form_valid(form)
