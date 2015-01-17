from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

from accounts import views


urlpatterns = patterns('',
    url(r'^$', views.NewUserView.as_view(), name='register'),
    url(r'^success/$', TemplateView.as_view(template_name="accounts/success.html"), name='success_created'),
    url(r'^activate/(?P<activation_key>\w+)/$', views.activate),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/$', views.LogInView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
)
