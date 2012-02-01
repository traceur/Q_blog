from django.conf.urls.defaults import patterns, include, url
from Q_blog.views import *
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Q_blog.views.home', name='home'),
    # url(r'^Q_blog/', include('Q_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',defaults),
    url(r'^atricle/(\d{0,9})',article),
    url(r'^page/(\d{0,9})',page),
)
