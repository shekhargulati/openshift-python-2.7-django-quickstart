from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
from django.conf import settings
if settings.DEBUG:    
urlpatterns += patterns('', (r'^media\/(?P<path>.*)$',
                                 'django.views.static.serve',
                                 {'document_root': settings.MEDIA_ROOT}),
                           )
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
