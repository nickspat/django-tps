from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from status_app import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.person_list, name='people_list'),
    url(r'^(?P<person_id>\w+)/$', views.person_detail, name='person_detail'),
    
)