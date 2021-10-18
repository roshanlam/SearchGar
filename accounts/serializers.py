from rest_framework import serializers
#from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active', 'created', 'updated']