from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('googleauth/', views.gauth, name='user_google_auth'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home' ),
    path('search/', views.search, name='search'),
    path('settings/', views.settings, name='settings'),
    path('savedLinks', views.savedLinks, name='savedLinks'),
    path('savedResults', views.savedResult, name='savedResults'),
    path('savedHistory', views.savedHistory, name='savedHistory'),
]
