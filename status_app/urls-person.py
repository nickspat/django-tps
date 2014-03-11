from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from status_app import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^(?P<person_id>\w+)/$', views.person_detail, name='person_detail'),

    url(r'^$', views.PersonList.as_view(), name='person_list'),
    url(r'^new$', views.PersonCreate.as_view(), name='person_new'),
    url(r'^edit/(?P<pk>\d+)$', views.PersonUpdate.as_view(), name='person_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.PersonDelete.as_view(), name='person_delete'),
 
       url(r'^status/(?P<status_id>\w+)/$', views.status_detail, name='status_detail'),
    url(r'^status/new$', views.StatusCreate.as_view(), name='status_new'),
    url(r'^status/edit/(?P<pk>\d+)$', views.StatusUpdate.as_view(), name='status_edit'),
    url(r'^status/delete/(?P<pk>\d+)$', views.StatusDelete.as_view(), name='status_delete'),
   
    
)