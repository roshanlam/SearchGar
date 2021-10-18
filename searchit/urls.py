from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('SearchEngine.urls')),
    path('', include('accounts.routers', 'accounts'), namespace='accounts-api'),
]
