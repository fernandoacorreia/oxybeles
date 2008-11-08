from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$',
        'oxybeles.views.new',
        name='oxybeles_new'),
    url(r'^(?P<uuid>[-0-9a-f]{36})/$',
        'oxybeles.views.detail',
        name='oxybeles_detail'),
)
