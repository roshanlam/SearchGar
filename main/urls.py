from django.conf.urls import url
from rest_framework.authtoken import views as drf_views
from . import views
urlpatterns = [
    url(r'^auth/$', drf_views.obtain_auth_token, name='auth'),
    url('', views.index, name='index')
]