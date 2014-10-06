from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'^$', 'example_project.views.home', name='home'),
    url(r'^jasmine/', include('django_jasmine.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
