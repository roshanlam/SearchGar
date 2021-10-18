from rest_framework.routers import SimpleRouter
from accounts.api import UserViewSet
from accounts.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet

routes = SimpleRouter()

routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

routes.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    *routes.urls
]
