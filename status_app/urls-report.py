from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from status_app import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.report_list, name='list'),
    url(r'^(?P<statusreport_id>\w+)/$', views.report_detail, name='report_detail'),
    
)