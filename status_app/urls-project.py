from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from status_app import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.project_list, name='list'),
    url(r'^(?P<project_id>\w+)/$', views.project_detail, name='team_detail'),
    
)