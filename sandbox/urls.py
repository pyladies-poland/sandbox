from django.conf.urls import patterns, include, url
from django.contrib import admin
import accounts.views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', accounts.views.NewUserView.as_view(), name='accounts'),
)
