from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home' ),
    path('search/', views.search, name='search'),
    path('submitWebsite/', views.crawlWebsite, name='crawlWebsite'),
    path('seeHistory/', views.seeHistory, name='SeeHistory')
]
