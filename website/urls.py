from django.conf.urls import url

from .views import home


app_name = 'website'

urlpatterns = [
    url(r'^$', home, name='home'),
]
