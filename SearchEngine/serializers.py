from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'])
        return user

class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = 'password'