from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^$', 'oxybeles.views.new', name="oxybeles_new"),
    #url(r'^(?P(.)+)/$', 'oxybeles.views.view', name="oxybeles_view"),
)

