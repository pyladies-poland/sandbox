from django.conf.urls import patterns, url

from places import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.PlaceDetailView.as_view(), name='place_detail'),
    )