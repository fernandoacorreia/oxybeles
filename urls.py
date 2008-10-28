from django.conf.urls.defaults import *
from oxybeles.models import PastedItem

info_dict = {
    'queryset': PastedItem.objects.all(),
    'slug_field': 'uuid',
}

urlpatterns = patterns('',
    url(r'^$', 'oxybeles.views.new', name='oxybeles_new'),
    url(r'^(?P<slug>[-0-9a-f]{36})/$',
        'django.views.generic.list_detail.object_detail', 
        info_dict, 
        'oxybeles_detail'),
)

