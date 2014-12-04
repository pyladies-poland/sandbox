from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

import accounts.views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', accounts.views.NewUserView.as_view(), name='accounts'),
    url(r'^accounts/success/', TemplateView.as_view(template_name="accounts/success.html")),
)
