from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('docs.views',

    url(r'^$','index'),
    url(r'^article/(?P<path>[\w-]+)/$','article'),
    url(r'^category/(?P<category_name>\w+)/$','category'),
    url(r'^index/$','article_index'),
    url(r'^search/$','search'),
    # Examples:
    # url(r'^$', 'docs.views.home', name='home'),
    # url(r'^docs/', include('docs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
