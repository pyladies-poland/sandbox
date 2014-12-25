import random, sha

from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.utils import timezone
from django.views import generic


from accounts.forms import NewUserForm, LogInForm
from accounts.models import User
from sandbox.settings import EMAIL_HOST_USER, HOST_NAME


class NewUserView(generic.CreateView):
    template_name = "accounts/new_account.html"
    success_url = reverse_lazy('accounts:success_created')
    form_class = NewUserForm

    def form_valid(self, form):
        new_user = form.save()
        new_user.set_password(form.cleaned_data["password"])
        salt = sha.new(str(random.random())).hexdigest()[:5]
        new_user.activation_key = sha.new(salt+new_user.name).hexdigest()
        new_user.save()
        subject = "SandboxApp: Confirm registration"
        text = "Hi %s, \n please confirm Your registration by clicking or copy-past this link \n" \
               "%s/accounts/activate/%s/ \n Please confirm with in 48 houers. Thank You for using our app."\
                " \n Your Sandbox Team" % (new_user.name, HOST_NAME, new_user.activation_key)
        send_mail(subject, text, EMAIL_HOST_USER, [new_user.email], fail_silently=False)
        return super(NewUserView, self).form_valid(form)


def activate(request, activation_key):
    profile = get_object_or_404(User, activation_key=activation_key)
    if profile.akey_expires < timezone.now():
        return render_to_response('accounts/activate.html', {'expired': True})
    profile.active = True
    profile.activation_key = ''
    profile.save()
    return render_to_response('accounts/activate.html', {'success': True})


class LogInView(generic.FormView):
    template_name = "accounts/login.html"
    form_class = LogInForm

    def form_valid(self, form):
        f = form
        email = f.cleaned_data['email']
        password = f.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user.active:
            login(self.request, user)
        return render_to_response('accounts/home.html', {'success': True})

#add later user decorator
class HomeView(generic.ListView):
    template_name = 'accounts/home.html'
    context_object_name = 'User_list'
    model = User


def logout_view(request):
    logout(request)
    return render_to_response('accounts/home.html', {'success': True})
