from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('submitWebsite/', views.crawlWebsite, name='crawlWebsite'),
    path('seeHistory/Query/', views.seeHistoryQuery, name='SeeHistoryQuery'),
    path('seeHistory/Crawl/', views.seeHistoryCrawl, name='SeeHistoryCrawl'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]