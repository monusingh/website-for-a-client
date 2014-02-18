from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hcaatc.views.home', name='home'),
    # url(r'^hcaatc/', include('hcaatc.foo.urls')),
    url(r'^$','hca.views.index'),
    url('^about/$','hca.views.about'),
    url('^our-mission/$','hca.views.about1'),
    url('^contact-us/$','hca.views.contact'),
    url('^courses/$','hca.views.course'),
    url('^c-language/$','hca.views.c'),
    url('^fee-structure/$','hca.views.fee'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls')),
)
