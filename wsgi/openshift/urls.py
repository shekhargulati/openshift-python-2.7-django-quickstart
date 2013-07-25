from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home', name='home'),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('', (r'^media\/(?P<path>.*)$',
                                 'django.views.static.serve',
                                 {'document_root': settings.MEDIA_ROOT}),
                           )

urlpatterns += staticfiles_urlpatterns()
