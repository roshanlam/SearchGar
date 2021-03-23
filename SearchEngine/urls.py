from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', views.user_login,name='user_login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home' ),
    path('home/admin/login/', views.adminLogin, name='adminLogin'),
    path('home/admin/home/', views.adminHome, name='adminHome'),
   # path('home/admin/addWebsite', views.addWebsite, name='addWebsite'),
    path('search/', views.search, name='search'),
    path('settings/', views.settings, name='settings'),
    path('savedLinks', views.savedLinks, name='savedLinks'),
    path('savedResults', views.savedResult, name='savedResults'),
    path('savedHistory', views.savedHistory, name='savedHistory'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('removeWebsite', views.removeWebsite, name='removeWebsite')
]