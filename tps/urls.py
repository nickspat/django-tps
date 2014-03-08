from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^project/', include('status_app.urls-project')),
    url(r'^team/', include('status_app.urls-team')),
    url(r'^person/', include('status_app.urls-person')),
    url(r'^reports/', include('status_app.urls-report')),
	#url(r'^$', RedirectView.as_view(url='/project', permanent=False), name='index')
 	url(r'^$', 'status_app.views.index', name='home')

    
)
