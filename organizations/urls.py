"""
URLS for organizations
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

# pylint: disable=invalid-name
urlpatterns = patterns(
    '',
    # Django Admin
    url(r'^admin/', include(admin.site.urls)),

    # Organizations urls
    url(r'^v0/', include('organizations.v0.urls', namespace='v0')),
)
