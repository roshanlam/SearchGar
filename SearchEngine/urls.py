from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home' ),
    path('search/', views.search, name='search'),
    path('submitWebsite/', views.crawlWebsite, name='crawlWebsite'),
    path('seeHistory/Query/', views.seeHistoryQuery, name='SeeHistoryQuery'),
    path('seeHistory/Crawl/', views.seeHistoryCrawl, name='SeeHistoryCrawl')
]
