from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import permission_required

from shorts.views import index, shorten


urlpatterns = patterns('',
    url(r'^$', index, name='shorts_index'),
    url(r'^shorten/$', shorten, name='shorts_shorten_url'),
)