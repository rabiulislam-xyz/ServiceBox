from django.conf.urls import url

from .views import home, search


app_name = 'website'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^search/$', search, name='search'),
]
