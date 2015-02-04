from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"), 
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^places/', include('places.urls', namespace='places'))
)
