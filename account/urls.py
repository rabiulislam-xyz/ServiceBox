from django.conf.urls import url

from .views import dashboard, update_profile


app_name = 'account' # namespace for this app

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^update/$', update_profile, name='update_profile'),
]
