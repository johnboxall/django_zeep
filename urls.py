from django.conf.urls.defaults import *

urlpatterns = patterns('django_zeep.views',
    (r'^callback/$', 'callback'),
)