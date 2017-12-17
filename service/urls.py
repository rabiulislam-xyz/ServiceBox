
from django.conf.urls import url

from .views import (ServiceCreate,
                    ServiceDetail,
                    ServiceList,
                    MyServiceList,
                    service_update,)

app_name = 'service'

urlpatterns = [
    url(r'add', ServiceCreate.as_view(), name='service_add'),
    url(r'update/(?P<pk>\d+)/', service_update, name='service_update'),
    url(r'list', ServiceList.as_view(), name='service_list'),
    url(r'my_service_list', MyServiceList.as_view(), name='my_service_list'),
    url(r'(?P<pk>\d+)/', ServiceDetail.as_view(), name='service_detail'),
]