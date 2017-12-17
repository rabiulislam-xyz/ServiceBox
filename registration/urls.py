from django.conf.urls import url
from django.contrib.auth.views import login, logout

from .views import user_signup


app_name = 'registration' # namespace for this app

urlpatterns = [
    url(r'^signup/$', user_signup, name='signup'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$',logout, {'next_page': '/'}, name='logout'),
]