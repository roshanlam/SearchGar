from django.urls import path, include
#from .views import RegisterView, LoginView, UserView, LogoutView
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views
from . import rest_api_view

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
]
