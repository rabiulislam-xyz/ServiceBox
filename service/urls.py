
from django.conf.urls import url

from .views import (service_create,
                    service_detial,
                    service_list,
                    my_service_list,
                    service_update,)

app_name = 'service'

urlpatterns = [
    url(r'^add/$', service_create, name='service_add'),
    url(r'^update/(?P<pk>\d+)/$', service_update, name='service_update'),
    url(r'^list/$', service_list, name='service_list'),
    url(r'^my_service_list/$', my_service_list, name='my_service_list'),
    url(r'^(?P<pk>\d+)/$', service_detial, name='service_detail'),
]