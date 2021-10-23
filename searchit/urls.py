from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from main import views as api_views

app_name = 'website'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SearchEngine.urls')),
]
