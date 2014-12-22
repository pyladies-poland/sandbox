from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
#from social_auth.views import

from accounts import views

urlpatterns = patterns('',
    url(r'^$', views.NewUserView.as_view(), name='accounts'),
    url(r'^success/$', TemplateView.as_view(template_name="accounts/success.html"), name='success_created'),
    url(r'^activate/(?P<activation_key>\w+)/$', views.activate),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/$', views.loginview),
    url(r'^logout/$', views.logoutview),
    #url(r'^logedin/$', views.home),
)
