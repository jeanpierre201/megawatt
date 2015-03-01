from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'megawatt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^sites/', include('sites.urls', namespace="sites")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summary/', include('summary.urls', namespace="summary")),
    url(r'^summary-average/', 'summary.views.average', name="summary-average"),
)
