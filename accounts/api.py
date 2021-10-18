#from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters



class UserViewSet(viewsets.ModeViewSet):
  http_method_names = ['get']
  serializer_class = UserSerializer
  permission_classes = (IsAuthenticated,)
  filter_backends = [filters.OrderingFilter]
  ordering_fields = ['updated']
  ordering = ['-updated']

  def get_queryset(self):
    return User.objects.all()

  def get_object(self):
    lookup_field_value = self.kwargs[self.lookup_field]
    obj = User.objects.get(id = lookup_field_value)
    self.check_object_permissions(self.request, obj)
    return obj