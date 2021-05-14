from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home' ),
    path('search/', views.search, name='search'),
    #path('settings/', views.settings, name='settings'),
    path('saveHistory/', views.saveHistory, name='saveHistory'),
    path('submitWebsite/', views.crawlWebsite, name='crawlWebsite'),
    #path('login', views.user_login, name='user_login'),
    #path('signup', views.user_signup, name='user_signup'),
]
