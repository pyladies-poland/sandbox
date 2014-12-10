from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from accounts import views

urlpatterns = patterns('',
    url(r'^$', views.NewUserView.as_view(), name='accounts'),
    url(r'^success/$', TemplateView.as_view(template_name="accounts/success.html"), name='success_created'),
    url(r'^activate/(?P<activation_key>\w+)/$', views.activate)
)
