from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', views.user_login,name='user_login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home' ),
    path('admin/login/', views.adminLogin, name='adminLogin'),
    path('admin/home/', views.adminHome, name='adminHome'),
    path('search', views.search, name='search'),
    path('settings/', views.settings, name='settings')
]