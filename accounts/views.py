import random, sha

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.utils import timezone
from django.views import generic


from accounts.forms import NewUserForm
from accounts.models import User
from sandbox.settings import EMAIL_HOST_USER, HOST_NAME


class NewUserView(generic.CreateView):
    template_name = "accounts/new_account.html"
    success_url = reverse_lazy('success_created')
    form_class = NewUserForm

    def form_valid(self, form):
        new_user = form.save()
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
    profile.is_active = True
    profile.activation_key = ''
    profile.save()
    return render_to_response('accounts/activate.html', {'success': True})


def loginview(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    if user.is_active:
        login(request, user)
    return render(request, 'accounts/login.html')


@login_required(login_url='/')
def home(request):
    return render_to_response('accounts/home.html')


def logoutview(request):
    logout(request)
    return redirect('/')
