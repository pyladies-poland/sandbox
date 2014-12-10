import datetime, random, sha

from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render_to_response
from django.views import generic

from accounts.forms import NewUserForm
from accounts.models import User
from sandbox.settings import EMAIL_HOST_USER



class NewUserView(generic.CreateView):
    template_name = "accounts/new_account.html"
    success_url = reverse_lazy('success_created')
    form_class = NewUserForm



    def form_valid(self, form):
        new_user = form.save()
        new_user.save()
        salt = sha.new(str(random.random())).hexdigest()[:5]
        new_user.activation_key = sha.new(salt+new_user.name).hexdigest()
        new_user.akey_expires = datetime.datetime.today() + datetime.timedelta(2)
        new_user.save()
        subject = "SandboxApp: Confirm registration"
        text = "Hi %s, \n please confirm Your registration by clicking or copy-past this link \n" \
               "./accounts/activate/%s/ \n Please confirm with in 48 houers. Thank You for using our app."\
                " \n Your Sandbox Team" % (new_user.name, new_user.activation_key)
        send_mail(subject, text, EMAIL_HOST_USER, [new_user.email], fail_silently=False)

        messages.success(self.request, "Congratulation You Created a User profile! Please check Your e-mail")
        return super(NewUserView, self).form_valid(form)


def activate(request, activation_key):
    profile = get_object_or_404(User, activation_key=activation_key)
    if profile.key_expires < datetime.datetime.today():
        return render_to_response('accounts/activate.html', {'expired': True})
    account = profile.user
    account.is_active = True
    account.save()
    return render_to_response('accounts/activate.html', {'success': True})
