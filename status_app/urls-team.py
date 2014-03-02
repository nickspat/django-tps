from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from status_app import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.team_list, name='index'),
    url(r'^(?P<team_id>\w+)/$', views.team_detail, name='team_detail'),
    
)