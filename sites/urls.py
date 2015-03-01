from django.conf.urls import patterns, url

from sites import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<site_id>\d+)/$', views.detail, name='detail'),
)