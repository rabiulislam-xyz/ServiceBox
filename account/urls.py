from django.conf.urls import url

from .views import profile, update_profile


app_name = 'account' # namespace for this app

urlpatterns = [
    url(r'^$', profile, name='profile'),
    url(r'^update/$', update_profile, name='update_profile'),
]
