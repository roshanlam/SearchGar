from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # Index Page - Tell Users To Create an Account or Login In
    url(r'^login$', views.login),
    url(r'^signup$', views.register),
    url(r'^home$', views.home)
]