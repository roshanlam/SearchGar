"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # Index Page - User Will Login
    url(r'^signup$', views.register),
    url(r'^home$', views.home),
    url(r'^user_login$', views.user_login)
]
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_signup, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('signup/', user_signup, name='user_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]